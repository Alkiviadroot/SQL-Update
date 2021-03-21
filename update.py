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
    for i in range(len(categories)):
        if(i==primaryKey):
            selectedIntication.append("P");
        else:
            selectedIntication.append(" ");
    end=False;
    while(not end):
        os.system('cls' if os.name == 'nt' else 'clear');
        print("Select colums - for multiple colums use comma (eg. 1,2,3...)");
        counter = 0;
        for info in categories:
            print(selectedIntication[counter] + " ["+str(counter)+"] "+info);
            counter+=1;
        numbers = input("Type \"end\" to stop: ");
        selected = numbers.split(",");
        for num in selected:
            if(num.lower()=="end"):
                end=True;
            else:
                num=int(num);
                if(selectedIntication[num]=="*"):
                    selectedIntication[num]=" ";
                elif(selectedIntication[num]==" "):
                    selectedIntication[num]="*";
    counter=0;
    final=[];
    for intication in selectedIntication:
        if (intication=="*"):
            final.append(counter);
        counter+=1;
    return final;


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
    correct=False;
    while(not correct):
        counter = 0;
        for info in categories:
            print("["+str(counter)+"] "+info);
            counter += 1;
        try:
            primaryKey = int(input("Put the number of the Primary Key: "));
            if(primaryKey>=0 and primaryKey<counter):
                correct=True;
            else:
                os.system('cls' if os.name == 'nt' else 'clear');
                print("Primary Key Incorrect");
        except Exception:
            os.system('cls' if os.name == 'nt' else 'clear');
            print("Primary Key Incorrect");
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