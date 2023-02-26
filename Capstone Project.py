#Program: eHP Calculator
#Author: Seth Weaver-Rosamilia
#Last date modified 2/26/23
#Calculates effective HP for the game League of Legends

#imports breezypython
from breezypythongui import EasyFrame

#establishes window layout
class eHP(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width = 600, height = 200, title = 'LoL eHP Calculator')
        
        
        topPanel = self.addPanel(row = 0, column = 0)

        baseHealthPanel = topPanel.addPanel(row = 0, column = 0)
        baseHealthLabel = baseHealthPanel.addLabel(text = "Enter Base HP", row = 0, column = 1)
        baseHealthInput = baseHealthPanel.addIntegerField(value = 0, row = 1, column = 1)
        baseHealthInput.grid(sticky = "NW")

        baseArmorPanel = topPanel.addPanel(row = 0, column = 1)
        baseArmorLabel = baseArmorPanel.addLabel(text = "Enter Base Armor", row = 0, column = 1)
        baseArmorInput = baseArmorPanel.addIntegerField(value = 0, row = 1, column = 1)
        baseArmorInput.grid(sticky = "NW")

        baseMRPanel = topPanel.addPanel(row = 0, column = 2)
        baseMRLabel = baseMRPanel.addLabel(text = "Enter Base MR", row = 0, column = 1)
        baseMRInput = baseMRPanel.addIntegerField(value = 0, row = 1, column = 1)
        baseMRInput.grid(sticky = "NW")
        

        midPanel = self.addPanel(row = 1, column = 0)

        bonusHealthPanel = midPanel.addPanel(row = 0, column = 0)
        bonusHealthLabel = bonusHealthPanel.addLabel(text = "Enter Bonus HP", row = 0, column = 1)
        bonusHealthInput = bonusHealthPanel.addIntegerField(value = 0, row = 1, column = 1)
        bonusHealthInput.grid(sticky = "NW")

        bonusArmorPanel = midPanel.addPanel(row = 0, column = 1)
        bonusArmorLabel = bonusArmorPanel.addLabel(text = "Enter Bonus Armor", row = 0, column = 1)
        bonusArmorInput = bonusArmorPanel.addIntegerField(value = 0, row = 1, column = 1)
        bonusArmorInput.grid(sticky = "NW")

        bonusMRPanel = midPanel.addPanel(row = 0, column = 2)
        bonusMRLabel = bonusMRPanel.addLabel(text = "Enter bonus MR", row = 0, column = 1)
        bonusMRInput = bonusMRPanel.addIntegerField(value = 0, row = 1, column = 1)
        bonusMRInput.grid(sticky = "NW")

        botPanel = self.addPanel(row = 2, column = 0)
        calcButton = botPanel.addButton(row = 0, column = 0, text = "Calculate", command = self.calculateTotals)
        calcButton.grid(sticky = "NSEW")

    def calculateTotals():
        baseHP = baseHealthInput.getNumber()
        bonusHP = bonusHealthInput.getNumber()
        totalHP = baseHP + bonusHP

        baseArmor = baseArmorInput.getNumber()
        bonusArmor = bonusArmorInput.getNumber()
        totalArmor = baseArmor + bonusArmor

        baseMR = baseMRInput.getNumber()
        bonusMR = bonusMRInput.getNumber()
        totalMR = baseMR + bonusMR

def main():
    eHP().mainloop()

if __name__ == "__main__":
    main()
