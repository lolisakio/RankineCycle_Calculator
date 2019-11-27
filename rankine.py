from CoolProp.CoolProp import PropsSI

fluid = raw_input("Type Fluid : ")
CoolPT = input("Type Cooler Pressure : ")
HighPT = input("Type Boiler Output Pressure : ")
HighTC = input("Type Boiler Output Tempreature(Degree Celcius) : ")

CoolP = CoolPT * 1000
HighP = HighPT * 1000
HighT = HighTC + 273

CoolOutH = PropsSI('H','P',CoolP,'Q',0,fluid)
CoolOutv = PropsSI('V','P',CoolP,'Q',0,fluid)

WPump = CoolOutv * (HighP - CoolP)

PumpOutH = CoolOutH + WPump

BoilerOutH = PropsSI('H','P',HighP,'T',HighT,fluid)
BoilerOutS = PropsSI('S','P',HighP,'T',HighT,fluid)

TurbOutH = PropsSI('H','P',CoolP,'S',BoilerOutS,fluid)

CoolerQ = PropsSI('Q','P',CoolP,'H',TurbOutH,fluid)

WTurb = BoilerOutH - TurbOutH

Qin = BoilerOutH - PumpOutH

nu = ((WTurb)-(WPump)) / (Qin)

print("Efficienty is :",nu)
print("CoolOutH is",CoolOutH)
print("CoolOutv is",CoolOutv)
print("TurbOutH is",TurbOutH)
print("BoilerOutH is",BoilerOutH)
print("BoilerOutS is",BoilerOutS)


print("Wpump is",WPump)
print("WTurb is",WTurb)
print("Qin is",Qin)
print("Quality of Cooler is",CoolerQ)
