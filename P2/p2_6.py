currentPrice =float(input("Enter the current price"))
purchasePrice = 2000 * 0.4
buyComm = purchasePrice*0.03
sellPrice = 2000 * currentPrice
sellComm = sellPrice *0.02
totalComm = buyComm + sellComm
print(f"You paid total commission of ${totalComm}")
print(f"You have made a profit of ${sellPrice-purchasePrice-totalComm}")