#Program to generate and calculate the invoice
#for St.Johns yatch Club 
#Date written : Sept 05 2023
#Author : SIREESHA KUPPAMPATI

#Declaring Constant Values
HST = 0.15
Processfee = 59.00
canfee = 0.6
Mondues = 75
EachMemCost = 5

#Entering the input values

MemName = input("Enter the Member name                     : ").upper()
StAddr = input("Enter the member street address           : ").upper() 
City = input("Enter the city                            : ").upper()
Provice = input("Enter the  province                       : ").upper()
PostalCode = input("Enter the postal code                     : ").upper() 
HomePh = input("Enter the member home phone(###-###-####) : ")
CellPh = input("Enter the member cell phone(###-###-####) : ")
AltMems = int(input("How many Alternative Members              : "))

#Using the IF-ELSE Statements

SiteNo = int(input("Enter the site number from(1 - 100)       : "))
EvenSite = SiteNo % 2
if EvenSite == 0:
    SiteType = "EVEN"
    SiteCost = 80
else:
    SiteType ="ODD"
    SiteCost = 120

print()
print(SiteNo)
print(SiteType)
print(SiteCost)
print()

WSclean = input("Would you like weekly site cleaning service(Y/N): ").upper()
WSService = 0
WScleanCost = 0
if  WSclean == "Y": 
    WSService = "YES"
    WScleanCost = 50
else:
    WSService = "NO"
    WScleanCost = 0 

print()    
print(WSService)
print(WScleanCost)    
print()

Video = input("Would you like the video surveillance service(Y/N): ").upper()
VideoCost = 0
VService = 0
if Video == "Y":
    VService = "YES"
    VideoCost = 35
else:
    VService = "NO"
    VideoCost = 0

print()
print(VService)
print(VideoCost)
print()

MemType = input("Enter membership type(S/E): ").upper()
Mondues = 0

if MemType == "S":
    MemberType = "STANDARD"
    Mondues = 75
else:
    MemberType = "EXECUTIVE"
    Mondues = 150

print()
print(MemberType) 
print(Mondues) 
print()  
CurrDate = input("Enter the current date(YYYY-MM-DD):    ")
    
#calculations
print()
print()       
Sitecharges = SiteCost + (AltMems * EachMemCost) 

EXtracharges = WScleanCost + VideoCost

Subtotal = Sitecharges + EXtracharges

SalesHST = Subtotal * HST

Totmoncharges = Subtotal + SalesHST

Totmonfee = Totmoncharges + Mondues

Totyearfee = Totmonfee * 12

Monpay = (Totyearfee + Processfee) / 12

Cancelfee = Sitecharges * 12 * canfee

print()
print()

print(f"                             St.John's Marina & Yatch Club")
print(f"                               Yearly Member Receipt")
print()
print(f"                   _____________________________________________________")
print()
print(f"                         Client Name and Address:")
print()

print(f"                         {MemName:<24s}")
print(f"                         {StAddr:<24s}")
print(f"                         {City:<5s},  {Provice:<2s}   {PostalCode:>6s} ")
print(f"                         Phone: {HomePh:<12s}(H)")
print(f"                                {CellPh:<12s}(C)")
print()

print(f"                         Site({SiteNo:<1d}):  {SiteCost:<3d}    Member Type: {MemberType:>9s}")
print()
print(f"                         Alternate Members:                 {AltMems:>2d}")
print(f"                         Weekly Site Cleaning:             {WSService:>3s}")
print(f"                         Video Surveillance:               {VService:>3s}")
print()

SitechargesDSP = "${:,.2f}".format (Sitecharges)
print(f"                         Site Charges:                   {SitechargesDSP:>8s}")

ExtrachargesDSP = "${:,.2f}".format (EXtracharges)
print(f"                         Extra Charges:                  {ExtrachargesDSP:>8s}")

print(f"                                                    -----------------")

SubtotalDSP = "${:,.2f}".format (Subtotal)
print(f"                         Subtotal:                       {SubtotalDSP:>8s}")

SalesHSTDSP = "${:,.2f}".format (SalesHST)
print(f"                         Sales Tax(HST):                   {SalesHSTDSP:>6s}")

print(f"                                                     -----------------")

TotmonchargesDSP = "${:,.2f}".format (Totmoncharges)
print(f"                         Total Monthly Charges:          {TotmonchargesDSP:>8s}")

MonduesDSP = "${:,.2f}".format (Mondues)
print(f"                         Monthly Dues:                    {MonduesDSP:>6s}")

print(f"                                                    ------------------")

TotmonfeeDSP = "${:,.2f}".format (Totmonfee)
print(f"                         Total Monthly Fees:              {TotmonfeeDSP:>6s}")

TotyearfeeDSP = "${:,.2f}".format (Totyearfee)
print(f"                         Total Yearly Fees:            {TotyearfeeDSP:>10s}")

MonpayDSP = "${:,.2f}".format (Monpay)
print(f"                         Monthly Payments:               {MonpayDSP:>8s}")
print()
print(f"                        ________________________________________________")
print()
print(f"                         Issued:{CurrDate:<10s}")
print(F"                         HST Reg No: 549-33-5849-4720-9885")
print()
CancelfeeDSP = "${:,.2f}".format (Cancelfee)
print(f"                         Cancellation Fee:              {CancelfeeDSP:>8s}")
print()



