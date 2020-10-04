#eng - i____7d
VERSION = "v0.3.1 (4/10/20)"

import colorama
import re
import time

def error(code, line):
    errors = {
        "0.0": "Invalid error code: <invalidCode>",
        "0.1": "<fileName> is not an .eng file",
        "0.2": "<fileName> does not exist",
        "0.3": "Internal compiler code error:\n<error>",
        "1.0": "Command not recognised: \"<command>\"",
        "1.1": "No variable name specified",
        "1.2": "No value specified",
        "1.3": "Unknown data type",
        "1.4": "Unknown variable \"<variable>\"",
        "1.5": "Incorrect value data type; expected <expectation> but instead got <reality>",
        "1.6": "Incorrect variable data type; expected <expectation> but instead got <reality>",
        "2.0": "Number of iterations must be above 0",
        "2.1": "Unexpected indent",
        "3.0": "Empty marker ID",
        "3.1": "Unknown marker ID \"<id>\"",
        "4.0": "Wait time must be above or equal to 0"
    }

    if not code in errors.keys():
        error = errors["0.0"].replace("<invalidCode>", code)
        return colorama.Fore.RED + f"eng error 0.0 on Line {str(line+1)}: {error}" + colorama.Style.RESET_ALL
        return

    return colorama.Fore.RED + f"eng error {code} on Line {str(line)}: {errors[code]}" + colorama.Style.RESET_ALL

def compiler(file):
    def noIndent(l):
        return l.replace("- ", "", 1).strip()

    def engDataToPyData(data):
        data = str(data)
        if data.startswith("-"): #negative
            if data[1:].isdecimal(): #integer
                return int(data)
            elif data[1:].split(".")[0].isdecimal() and data[1:].split(".")[1].isdecimal(): #float
                return float(data)
        elif data.isdecimal(): #integer positive
            return int(data)
        elif data.split(".")[0].isdecimal() and data.split(".")[1].isdecimal(): #float positive
            return float(data)
        elif data[0] == "\"" and data[-1] == "\"": #string
            return data[1:-1]
        elif data == "yes" or data == "no": #boolean
            return True if data == "yes" else False
        else:
            print(error("1.3", lineno))
            return TypeError

    def pyDataToEngData(data):
        if isType(data, [bool]):
            return "yes" if data else "no"
        else:
            return str(data)
    
    def isType(var, types):
        return True if type(var) in types else False

    def pyTypeToEngType(t):
        if t == int:
            return "Whole Number"
        elif t == float:
            return "Decimal"
        elif t == str:
            return "Text"
        elif t == bool:
            return "Yes/No"

    f = open(file, "r").read().split("\n")
    f.append("note:")
    variables = {}
    indent = 0
    lineno = 1
    indenters = []
    commented = False

    while lineno < len(f)+1:
        line = f[lineno-1]

        #indents
        spaces = line.split("- ")[0]
        if (spaces.isspace() or spaces == "") and line.startswith(spaces+"- "):
            currentIndent = len(spaces)/2+1
        else:
            currentIndent = 0
        if indent < currentIndent:
            print(error("2.1", lineno))
            lineno += 1
            continue
        a = False
        while indent > currentIndent and not a and len(indenters) > 0:
            if indenters[0]["type"] == "forever":
                lineno = indenters[0]["goto"]
                a = True
            elif indenters[0]["type"] == "repeat":
                if indenters[0]["left"] > 1:
                    lineno = indenters[0]["goto"]
                    indenters[0]["left"] -= 1
                    a = True
                else:
                    indent -= 1
                    indenters.pop(0)
        if a:
            continue

        #block comments
        if noIndent(line).startswith("long notes ==="):
            commented = not commented
            lineno += 1
            continue
        if commented:
            lineno += 1
            continue

        #comments, whitespace, markers
        if line.strip() == "*":
            print(error("3.0", lineno))
            lineno += 1
            continue
        elif noIndent(line) == "" or noIndent(line).startswith("note:") or noIndent(line).startswith("* "):
            lineno += 1
            continue                

        #replacing variables
        for i in range(0, len(variables)):
            name = list(variables.keys())[i]
            value = variables[name]
            line = line.replace(f"<{name}>", str(pyDataToEngData(value)))
        if re.search("(?<=<)(.*)(?=>)", line) != None:
            print(error("1.4", lineno).replace("<variable>", re.search("(?<=<)(.*)(?=>)", line).group(0)))
            lineno += 1
            continue
        
        #print
        elif noIndent(line).startswith("say"):
            if engDataToPyData(noIndent(line).replace("say ", "", 1)) == TypeError:
                print(error("1.3", lineno))
                lineno += 1
                continue
            else:
                printed = engDataToPyData(noIndent(line).replace("say ", "", 1))
            print(pyDataToEngData(printed))

        #variables
        elif noIndent(line).startswith("let") or noIndent(line).startswith("set"):
            if re.search("(?<=let \')(.*)(?=\' be)", noIndent(line)) == None and re.search("(?<=set \')(.*)(?=\' to)", noIndent(line)) == None:
                print(error("1.1", lineno))
                lineno += 1
                continue
            varName = re.search("(?<=let \')(.*)(?=\' be)", noIndent(line)).group(0) if noIndent(line).startswith("let") else re.search("(?<=set \')(.*)(?=\' to)", noIndent(line)).group(0)
            

            rest = noIndent(line).replace(f"let '{varName}' be ", "", 1).replace(f"set '{varName}' to ", "", 1).strip()
            if rest == noIndent(line):
                print(error("1.2", lineno))
                lineno += 1
                continue

            if engDataToPyData(rest) == TypeError:
                lineno += 1
                continue
            else:
                variables[varName] = engDataToPyData(rest)

        #operate on variables
        elif noIndent(line).startswith("add") or noIndent(line).startswith("subtract"):
            mode = noIndent(line).split(" ")[0]

            if re.search("(?<=add )(.*)(?= to)", noIndent(line)) == None and re.search("(?<=subtract )(.*)(?= from)", noIndent(line)) == None:
                print(error("1.2", lineno))
                lineno += 1
                continue
            if mode == "add":
                value = re.search("(?<=add )(.*)(?= to)", noIndent(line)).group(0)
            elif mode == "subtract":
                value = re.search("(?<=subtract )(.*)(?= from)", noIndent(line)).group(0)
            if engDataToPyData(value) == TypeError:
                lineno += 1
                continue
            elif not isType(engDataToPyData(value), [int, float]): 
                print(error("1.5", lineno).replace("<expectation>", "Whole Number/Decimal").replace("<reality>", pyTypeToEngType(type(engDataToPyData))))
                lineno += 1
                continue
            else:
                valuePy = engDataToPyData(value)

            if not ((f"add {value} to \'" in line or f"subtract {value} from \'" in line) and line.endswith("\'")):
                print(error("1.1", lineno))
                lineno += 1
                continue

            variable = noIndent(line).replace(f"add {value} to \'", "", 1).replace(f"subtract {value} from \'", "", 1)[:-1]

            if not variable in variables.keys():
                print(error("1.4", lineno).replace("<variable>", variable))
                lineno += 1
                continue
            
            elif not isType(variables[variable], [int, float]): 
                print(error("1.6", lineno).replace("<expectation>", "Whole Number/Decimal").replace("<reality>", pyTypeToEngType(type(variables[variable]))))
                lineno += 1
                continue
            if mode == "add":
                variables[variable] = variables[variable] + valuePy
            elif mode == "subtract":
                variables[variable] = variables[variable] - valuePy


        #repeat
        elif noIndent(line).startswith("repeat"): 
            if noIndent(line) == "repeat forever:":
                indenters.insert(0, {"indent": indent+1, "goto": lineno+1, "type": "forever"})
                indent += 1
            else:
                repeats = noIndent(line).replace("repeat ", "", 1).replace(" times:", "", 1)
                if engDataToPyData(repeats) == TypeError:
                    lineno += 1
                    continue
                elif not isType(engDataToPyData(repeats), [int]): 
                    print(error("1.5", lineno).replace("<expectation>", "Whole Number").replace("<reality>", pyTypeToEngType(type(engDataToPyData(repeats)))))
                    lineno += 1
                    continue
                elif engDataToPyData(repeats) < 1:
                    print(error("2.0", lineno))
                    lineno += 1
                    continue
                else:
                    times = engDataToPyData(repeats)
                indenters.insert(0, {"indent": indent+1, "left": times, "goto": lineno+1, "type": "repeat"})
                indent += 1

        #throw error
        elif noIndent(line).startswith("throw error"):
            code = noIndent(line).replace("throw error ", "", 1)
            print(error(code, lineno))

        #jump to markers
        elif noIndent(line).startswith("jump to"):
            marker = noIndent(line).replace("jump to ", "", 1)
            if marker == "":
                print(error("1.2", lineno))
            skip = False
            for l in f:
                if noIndent(l).startswith("* " + marker):
                    lineno = f.index(l)+1
                    spaces = l.split("- ")[0]
                    if (spaces.isspace() or spaces == "") and l.startswith(spaces+"- "):
                        indent = len(spaces)/2+1
                    else:
                        indent = 0
                    
                    while len(indenters) > 0 and indenters[0]["indent"] > indent:
                        indenters.pop(0)

                    skip = True
            if skip:
                continue
            else:
                print(error("3.1", lineno).replace("<id>", marker))     

        #wait
        elif noIndent(line).startswith("wait"):
            if re.search("(?<=wait for )(.*)(?= millisecond)", noIndent(line)) == None and re.search("(?<=wait for )(.*)(?= second)", noIndent(line)) == None:
                print(error("1.2", lineno))
                lineno += 1
                continue
            if noIndent(line).endswith("milliseconds") or noIndent(line).endswith("millisecond"):
                s = re.search("(?<=wait for )(.*)(?= millisecond)", noIndent(line)).group(0)
            elif noIndent(line).endswith("second") or noIndent(line).endswith("seconds"):
                s = re.search("(?<=wait for )(.*)(?= second)", noIndent(line)).group(0)
            if engDataToPyData(s) == TypeError:
                lineno += 1
                continue
            elif not isType(engDataToPyData(s), [int, float]): 
                print(error("1.5", lineno).replace("<expectation>", "Whole Number/Decimal").replace("<reality>", pyTypeToEngType(type(engDataToPyData(s)))))
                lineno += 1
                continue
            elif engDataToPyData(s) < 0:
                print(error("4.0", lineno))
                lineno += 1
                continue
            else:
                sPy = engDataToPyData(s)
                if noIndent(line).endswith("milliseconds") or noIndent(line).endswith("millisecond"):
                    sPy = sPy / 1000

            time.sleep(sPy)

        #not recognised
        else:
            print(error("1.0", lineno).replace("<command>", noIndent(line)))
        
        lineno += 1

