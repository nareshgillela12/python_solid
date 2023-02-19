
from abc import ABC,abstractmethod

class Custtype(ABC):
    @abstractmethod
    def is_retailcust(self)->bool:
        pass
class Typeofcust(Custtype):

    retailcust=False

    def checkcusttype(self,cust):
        print("reatil cust")
        self.retailcust=True

    def is_retailcust(self) ->bool:
        return self.retailcust

class Customers(ABC):
    def __init__(self,custname):
        self.custname=custname
    @abstractmethod
    def getaddress(self,name1,name2,state):
        pass

class IndianCust(Customers):
    def __init__(self,name,cust:Custtype):
        self.custtype=cust
        self.name=name
    def getaddress(self,name,surname,state):
        print(f"Indian Addess {name} {surname}",state)
        if self.custtype.is_retailcust():
            print("retail cust")
        else:
            print(" b2b cust")

class USCust(Customers):
    def __init__(self,fname):
        self.name=fname
    def getaddress(self,name1,name2,state):
        print(f"US Address {name1} {name2}",state)

class CustomCharges(ABC):
    def __init__(self,taxam):
        self.taxam=taxam
    @abstractmethod
    def taxapplicable(self)->str:
        pass
class TaxAdd(CustomCharges):
    taxapplicable="0"
    def AddingTax(self,amount):
        print(f"Added tax is {amount}")
        taxapplicable=amount
    def is_taxapplicable(self) ->str:
        return self.taxapplicable

class Orders(ABC):
    def __init__(self,ordertype):
        self.ordertype=ordertype
    @abstractmethod
    def placeorder(self,quan,price):
        pass

class NormalOrders(Orders):
    def __init__(self,shipspped,tax:CustomCharges):
        self.tax=tax
        self.shipspeed=shipspped
    def placeorder(self,quan,price):
        print(f"Normal order total is {quan*price}")
        if((price*quan)>24):
            taxcal=self.tax.taxam
            print(f"Including Tax is {(price*quan)+int(taxcal)}")
        else:
            print("No tax Added")

class ScheduledOrders(Orders):
    def __init__(self,scheduleddate):
        self.scheduleddate=scheduleddate
    def placeorder(self,quan,price):
        print(f"Scheduled order total is {price*quan}")


class CustomLengths(ABC):
    @abstractmethod
    def is_sizeexists(self)->bool:
        pass
class PromoLength(CustomLengths):
    sizeexists=False
    def checkproductsize(self,size):
        print(f"Exists for {size} size")
        self.sizeexists=True
    def is_sizeexists(self) ->bool:
        return self.sizeexists

class Products(ABC):
    def __init__(self,productval):
        self.productval=productval
    @abstractmethod
    def loadproducts(self,producttype):
        pass

class Electronics(Products):
    def __init__(self,specifications):
        self.specifications=specifications
    def loadproducts(self,producttype):
        print(f"Loading {producttype}")

class PromotionalIProducts(Products):
    def __init__(self,messurments,size:CustomLengths):
        self.size=size
        self.messurments=messurments
    def loadproducts(self,producttype):
        if not self.size.is_sizeexists():
            raise Exception("No Item exists")
        print(f"Loding {producttype}")

class Shippers(ABC):

    def __init__(self,baseval):
        self.baseval=baseval

    @abstractmethod
    def get_shipper(self,shipping_state):
        pass

class Tracking(ABC):
    @abstractmethod
    def trackurlexists(self)->bool:
        pass

class TrackItem(Tracking):
    istrackitem=False

    def showingtrackurl(self,url):
        print(f"track url is {url}")
        self.istrackitem=True

    def trackurlexists(self) -> bool:
        return self.istrackitem

class AndraShipper(Shippers):

    def __init__(self,privateship):
        self.peship=privateship

    def get_shipper(self,shipping_state):
        print(f"AP Shipper {self.peship}",shipping_state)

class TelanganaShipper(Shippers):

    def __init__(self,southindia,trackitem:Tracking):
        self.southindia=southindia
        self.trackitem=trackitem

    def get_shipper(self,shipping_state):
        if not self.trackitem.trackurlexists():
            raise Exception("no track url")
        print(f"TS Shipper {self.southindia}",shipping_state)

psize=PromoLength()
promoitem=PromotionalIProducts("Gents",psize)
psize.checkproductsize("L")
promoitem.loadproducts("Shirt")

electronics=Electronics("Chargable")
electronics.loadproducts("TVs")

tax=TaxAdd(10)
normalorder=NormalOrders("1 day",tax)
tax.AddingTax(10)
normalorder.placeorder(4,10)

schedorder=ScheduledOrders("12/12/12")
schedorder.placeorder(2,4)

cus=Typeofcust()
cuss=IndianCust("test",cus)
cus.checkcusttype("retail")
cuss.getaddress("t1","s1","TS")

uscust=USCust("fn")
uscust.getaddress("ff","ll","FL")


# Telangana
track=TrackItem()
shipper=TelanganaShipper("South India",track)
track.showingtrackurl("https://trackitem")
shipper.get_shipper("Telangana")

# Andra
shipper=AndraShipper("South India")
shipper.get_shipper("Andra")