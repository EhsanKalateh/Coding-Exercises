print('Enter "Done" to stop the program')
while True:
    Sex=input ("Male, Female, Infant \U0001FA78\n")
    if Sex.lower()[0]=="d":
        break
    Test=input("Which? MCV/MCH/MCHC\n")
    #MCV
    if Test.lower()=="mcv":
        #HCT
        HCT_Percent=float(input ("HCT %= "))
        if HCT_Percent>60: #HCT Danger
            print("DANGER!")
        elif HCT_Percent<15: #HCT Danger
            print("DANGER!")        
        elif Sex!="": #Range HCT
            if list (Sex.lower())[0]=="m":
                if HCT_Percent>52:
                    print("High HCT")
                elif HCT_Percent<42:
                    print ("Low HCT")
                else:
                    print ("Normal HCT")
            elif list (Sex.lower())[0]=="f":
                if HCT_Percent>47:
                    print("High HCT")
                elif HCT_Percent<37:
                    print ("Low HCT")
                else:
                    print ("Normal HCT")

            elif list (Sex.lower())[0]=="i":
                #Age_Infant=input
                #
                #
                print ("For New Borns up to 60%\ is Normal and for 1month old and 1year old infants, between 36-40%")
        #RBC:
        RBC_Count=float(input("RBC Count= "))
        if Sex!="": #Range RBC
            if list (Sex.lower())[0]=="m":
                if RBC_Count>6:
                    print("Polycytemia")
                elif RBC_Count<4.6:
                    print ("Anemia")
                else:
                    print ("Normal RBC Count")
            elif list (Sex.lower())[0]=="f":
                if RBC_Count>5:
                    print("Polycytemia")
                elif RBC_Count<4.2:
                    print ("Anemia")
                else:
                    print ("Normal RBC Count")
        mcv=(HCT_Percent*10/RBC_Count)
        print (f"MCV= {round(mcv, 2)} fL")
        if True: #MCV Range
            if mcv>96:
                print("Macrocytemia")
            elif mcv<80:
                print("Microcytemia")
            else:
                print("Normal Corpuscular Volume")
        print ("_________\n")

    #MCH
    elif Test.lower()=="mch":
        #HGB
        Hb=float(input ("Hb= "))
        if Sex!="": #Range HGB
            if list (Sex.lower())[0]=="m":
                if Hb>16:
                    print("High HGB")
                elif Hb<13:
                    print ("Low HGB")
                else:
                    print ("Normal HGB")
            elif list (Sex.lower())[0]=="f":
                if Hb>15:
                    print("High HGB")
                elif Hb<12:
                    print ("Low HGB")
                else:
                    print ("Normal HGB")
            elif list (Sex.lower())[0]=="i":
                if Hb>20:
                    print("High HGB")
                elif Hb<18:
                    print ("Low HGB")
                else:
                    print ("Normal HGB")
        #RBC
        RBC_Count=float(input("RBC Count= ")) 
        if Sex!="": #Range RBC
            if list (Sex.lower())[0]=="m":
                if RBC_Count>6:
                    print("Polycytemia")
                elif RBC_Count<4.6:
                    print ("Anemia")
                else:
                    print ("Normal RBC Count")
            elif list (Sex.lower())[0]=="f":
                if RBC_Count>5:
                    print("Polycytemia")
                elif RBC_Count<4.2:
                    print ("Anemia")
                else:
                    print ("Normal RBC Count")
        mch=Hb*10/RBC_Count
        print (f"MCH= {round(mch, 2)} pg")
        if True: #Range MCH
            if mch>32:
                print("MCH (Mean Carpuscular Hemoglobin) is 'HIGH'")
            elif mch<23:
                print("MCH (Mean Carpuscular Hemoglobin) is 'LOW'")
            else:
                print("MCH (Mean Carpuscular Hemoglobin) is 'NORMAL'")
        print ("_________\n")

    #MCHC
    elif Test.lower()=="mchc":
        Hb=float(input ("Hb= ")) 
        if Sex!="": #Range HGB
            if list (Sex.lower())[0]=="m":
                if Hb>16:
                    print("High HGB")
                elif Hb<13:
                    print ("Low HGB")
                else:
                    print ("Normal HGB")
            elif list (Sex.lower())[0]=="f":
                if Hb>15:
                    print("High HGB")
                elif Hb<12:
                    print ("Low HGB")
                else:
                    print ("Normal HGB")
            elif list (Sex.lower())[0]=="i":
                if Hb>20:
                    print("High HGB")
                elif Hb<18:
                    print ("Low HGB")
                else:
                    print ("Normal HGB")
        HCT_Percent=float(input ("HCT%= "))
        if HCT_Percent>60: #HCT Danger
            print("DANGER!")
        elif HCT_Percent<15: #HCT Danger
            print("DANGER!")        
        elif Sex!="": #Range HCT
            if list (Sex.lower())[0]=="m":
                if HCT_Percent>52:
                    print("High HCT")
                elif HCT_Percent<42:
                    print ("Low HCT")
                else:
                    print ("Normal HCT")
            elif list (Sex.lower())[0]=="f":
                if HCT_Percent>47:
                    print("High HCT")
                elif HCT_Percent<37:
                    print ("Low HCT")
                else:
                    print ("Normal HCT")

            elif list (Sex.lower())[0]=="i":
                #Age_Infant=input
                #
                #
                print ("For New Borns up to 60%\ is Normal and for 1month old and 1year old infants, between 36-40%")
        mchc=Hb*100/HCT_Percent
        print (f"MCHC= {round(mchc, 2)} g/dL")
        if True: #Range MCHC
            if mchc>38:
                print("MCHC  is 'HIGH'")
            elif mchc<32:
                print("MCHC is 'LOW'")
            else:
                print("MCHC is 'NORMAL'")
        print ("_________\n")

    elif Test.lower()[0]=="d":
        break
    else:
        print ("Again")
