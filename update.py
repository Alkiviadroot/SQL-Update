import os
import csv


def loadFile(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',');
        first = True;
        data = [];
        for row in csv_reader:
            if(first):
                categories = row;
                first = False;
            else:
                data.append(row);
    csv_file.close();
    return(categories, data);


def generateScript(tableName, primaryKey, selectedColums, databaseNames, data,primaryKeyNum):
    filename=tableName+"-update.sql";
    file = open(filename, "w");
    file = open(filename, "a");
    for x in data:
        file.write("UPDATE " + tableName+" SET\n");
        counter = 0;
        for num in selectedColums:
            if(str(x[int(num)])!=""):
                if(counter==len(databaseNames)-1):
                    file.write(str(databaseNames[counter])+ " = '"+ str(x[int(num)]+"'\n" ));
                else:
                    file.write(str(databaseNames[counter])+ " = '"+ str(x[int(num)]+"',\n" ));
            counter+=1;
        file.write("WHERE "+ str(primaryKey)+" = "+str(x[primaryKeyNum])+";\n\n");
    file.close();
    print("Script "+filename+" created");


def selectColums(categories, primaryKey):
    selectedIntication=[];
    for i in range(categories.len()):
        if(i==primaryKey):
            selectedIntication.append["P"];
        else:
            selectedIntication.append[""];
    os.system('cls' if os.name == 'nt' else 'clear');
    counter = 0;
    for info in categories:
        print(selectedIntication + " ["+str(counter)+"] "+info);
    
    
    # end=True;
    # while(end):
    #     os.system('cls' if os.name == 'nt' else 'clear');
    #     print("Primary Key: ["+str(primaryKey)+"] "+categories[primaryKey]);
    #     counter = 0;
    #     selected=[];
    #     for info in categories:
    #         if(info != categories[primaryKey]):
    #             for x in selected:
    #                 print("* ["+str(counter)+"] "+info)
    #             print("  ["+str(counter)+"] "+info);
    #         counter += 1;
    #     numbers = input("Give all the colums separated by comma (eg. 1,4,5...): ");
    #     selected = numbers.split(",");
    # return selected;


def matchToDatabase(colums, categories):
    os.system('cls' if os.name == 'nt' else 'clear');
    print("Match colums to Database");
    databaseNames = [];
    for x in colums:
        name=input(categories[int(x)]+": ");
        if(name==""):
            databaseNames.append(categories[int(x)]);
        else:
            databaseNames.append(name);
    return databaseNames;


def getPrimary(categories):
    counter = 0;
    for info in categories:
        print("["+str(counter)+"] "+info);
        counter += 1;
    primaryKey = int(input("Put the number of the Primary Key: "));
    return primaryKey;


def main():
    fileCsv=input("Give the path of CSV file: ");
    arrays = loadFile(fileCsv);
    categories = arrays[0];
    data = arrays[1];
    tableName = input("Database-Table name: ");
    primaryKey = getPrimary(categories);
    selectedColums = selectColums(categories, primaryKey);
    databaseNames = matchToDatabase(selectedColums, categories);
    generateScript(tableName, categories[primaryKey], selectedColums, databaseNames, data,primaryKey);
    
    
if(__name__=="__main__"):
    main();