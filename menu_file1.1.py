######### Baue ein Hauptmenü mit Unterkategorien aus #########
########################
######### 

run_menu = True
run_container_menu = True
run_gibo_menu = True

user_input  = ""
#MENÜLOOP
while run_menu:
    #Hauptmenü
    print("# BESTANDSHAUPTMENÜ\n\n\t1 - CONTAINER\n\t2 - GITTERBOXEN\n\tQ - BEENDEN")
    user_input = input("\t")
    #MENÜVERZWEIGUNG
    if user_input == "1":
        #CONTAINERBESTAND
        while run_container_menu:
          
            print ("# CONTAINER\n\n\tSG1 - KÜHLSCHRÄNKE\n\tSG2 - BILDSCHIRME\n\tSG4 - GROßGERÄTE\n\tSG5 - KLEINGERÄTE\n\tZ - ZURÜCK")
            user_input = input("\t")
            if user_input.upper() == "SG1":
                #SAMMELGRUPPE 1 
                while True:
                  
                    print("# SAMMELGRUPPE 1 - KÜHLGERÄTE\n\n# AKTUELLER BESTAND:\tGRÜN:0\tROT:0\n#\n#\n\tADD - CONTAINER HINZUFÜGEN\n\tDEL - CONTAINER LÖSCHEN\n\tZ - ZURÜCK")
                    user_input = input("\t")
                    ######## HIER SOLL DANNN MIT ARRAYS GEARBEITET WERDEN BZW DATENBANK #####
                    if user_input.upper() == "ADD":
                        print ("\n\t WURDE HINZUGEFÜGT\n\n")
                    elif user_input.upper() == "DEL":
                        print ("\n\t WURDE GELÖSCHT\n\n")
                    elif user_input.upper() == "Z":
                        break
                    else:
                        for i in range(2, 0, -1):
                            user_input = input("\t")
                        break

            #SAMMELGRUPPE 2 
            elif user_input.upper() == "SG2":
                while True:

                    print("# SAMMELGRUPPE 2 - BILDSCHIRME\n\n# AKTUELLER BESTAND:\tGRÜN:0\tROT:0\n#\n#\n\tADD - CONTAINER HINZUFÜGEN\n\tDEL - CONTAINER LÖSCHEN\n\tZ - ZURÜCK")
                    user_input = input("\t")
                    ######## HIER SOLL DANNN MIT ARRAYS GEARBEITET WERDEN BZW DATENBANK #####

                    if user_input.upper() == "ADD":
                        print ("\n\t WURDE HINZUGEFÜGT\n\n")
                    elif user_input.upper() == "DEL":
                        print ("\n\t WURDE GELÖSCHT\n\n")
                    elif user_input.upper() == "Z":
                        break
                    else:
                        for i in range(2, 0, -1):
                            user_input = input("\t")
                        break
            
            #SAMMELGRUPPE 4 
            elif user_input.upper() == "SG4":
                while True:

                    print("# SAMMELGRUPPE 4 - GROßGERÄTE\n\n# AKTUELLER BESTAND:\tGRÜN:0\tROT:0\n#\n#\n\tADD - CONTAINER HINZUFÜGEN\n\tDEL - CONTAINER LÖSCHEN\n\tZ - ZURÜCK")
                    user_input = input("\t")
                    ######## HIER SOLL DANNN MIT ARRAYS GEARBEITET WERDEN BZW DATENBANK #####

                    if user_input.upper() == "ADD":
                        print ("\n\t WURDE HINZUGEFÜGT\n\n")
                    elif user_input.upper() == "DEL":
                        print ("\n\t WURDE GELÖSCHT\n\n")
                    elif user_input.upper() == "Z":
                        break
                    else:
                        for i in range(2, 0, -1):
                            user_input = input("\t")
                        break
            
            #SAMMELGRUPPE 5 
            elif user_input.upper() == "SG5":
                while True:

                    print("# SAMMELGRUPPE 5 - GROßGERÄTE\n\n# AKTUELLER BESTAND:\tGRÜN:0\tROT:0\n#\n#\n\tADD - CONTAINER HINZUFÜGEN\n\tDEL - CONTAINER LÖSCHEN\n\tZ - ZURÜCK")
                    user_input = input("\t")
                    ######## HIER SOLL DANNN MIT ARRAYS GEARBEITET WERDEN BZW DATENBANK #####

                    if user_input.upper() == "ADD":
                        print ("\n\t WURDE HINZUGEFÜGT\n\n")
                    elif user_input == "DEL":
                        print ("\n\t WURDE GELÖSCHT\n\n")
                    elif user_input.upper() == "Z":
                        break
                    else:
                        for i in range(2, 0, -1):
                            user_input = input("\t")
                        break
            
          
            elif user_input.upper() == "Z":
                break
            else:
                for i in range(2, 0, -1):
                    user_input = input("\t")
                break

                
    #GITTERBOXEN MENü
    elif user_input == "2":
        print ("# GITTERBOXEN\n")

    elif user_input.upper()  == "Q":
        print("\n\t# PROGRAMM BEENDET\n\n")
        run_menu = False
    
    else:
        #3 VERSUCHE BIS DAS PROGRAMM BEENDET
        for i in range(3, 0, -1):
            user_input = input("\t")
            
        run_menu = False
        print("\nPROGRAMM BEENDET")
    
