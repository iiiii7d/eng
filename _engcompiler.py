import colorama
import re

def error(code, line):
    errors = {
        "0.0": "Invalid error code: <invalidCode>",
        "0.1": "<fileName> is not an .eng file",
        "0.2": "Internal compiler code error:\n<error>",
        "1.0": "Command not recognised: \"<command>\"",
        "1.1": "No variable name specified",
        "1.2": "No value specified",
        "1.3": "Unknown data type",
        "1.4": "Unknown variable \"<variable>\"",
        "1.5": "Incorrect data type",
        "2.0": "Number of iterations must be above 0",
        "2.1": "Unexpected indent"
    }

    if not code in errors.keys():
        error = errors["0.0"].replace("<invalidCode>", code)
        return colorama.Fore.RED + f"eng error 0.0 on Line {str(line+1)}: {error}" + colorama.Style.RESET_ALL
        return

    return colorama.Fore.RED + f"eng error {code} on Line {str(line)}: {errors[code]}" + colorama.Style.RESET_ALL

def compiler(file):
    f = open(file, "r").read().split("\n")
    f.append("note:")
    variables = {}
    indent = 0
    lineno = 1
    indenters = []

    def noIndent(l):
        return l.replace("- ", "", 1).strip()

    def engDataToPyData(data):
        if data[0] == "\"" and data[-1] == "\"": #string
            return data[1:-1]
        elif data.startswith("-"): #negative
            if data[1:].isdecimal(): #integer
                return int(data)
            elif data[1:].split(".")[0].isdecimal() and data[1:].split(".")[1].isdecimal(): #float
                return float(data)
        elif data.isdecimal(): #integer positive
            return int(data)
        elif data.split(".")[0].isdecimal() and data.split(".")[1].isdecimal(): #float positive
            return float(data)
        elif data == "yes" or data == "no": #boolean
            return True if data == "yes" else False
        else:
            print(error("1.3", lineno))
            return TypeError

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
        while indent > currentIndent and not a:
            if indenters[0]["type"] == "repeat":
                if indenters[0]["left"] > 1:
                    lineno = indenters[0]["goto"]
                    indenters[0]["left"] -= 1
                    a = True
                else:
                    indent -= 1
                    indenters.pop(0)
        if a:
            continue

        #comments
        if noIndent(line) == "" or line.startswith("note:"):
            lineno += 1
            continue                

        #replacing variables
        for i in range(0, len(variables)):
            name = list(variables.keys())[i]
            value = variables[name]
            line = line.replace(f"<{name}>", str(value))
        if re.search("(?<=<)(.*)(?=>)", line) != None:
            print(error("1.4", lineno).replace("<variable>", re.search("(?<=<)(.*)(?=>)", line).group(0)))
            lineno += 1
            continue
        
        #print
        elif noIndent(line).startswith("say"):
            if engDataToPyData(noIndent(line).replace("say ", "")) == TypeError:
                lineno += 1
                continue
            else:
                printed = engDataToPyData(noIndent(line).replace("say ", ""))
            print(printed)

        #variables
        elif noIndent(line).startswith("let"):
            if re.search("(?<=let \')(.*)(?=\' be)", noIndent(line)) == None:
                print(error("1.1", lineno))
                lineno += 1
                continue
            varName = re.search("(?<=let \')(.*)(?=\' be)", noIndent(line)).group(0)

            rest = noIndent(line).replace(f"let '{varName}' be ", "").strip()
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
                print(error("1.3", lineno))
                lineno += 1
                continue
            elif not (isinstance(engDataToPyData(value), int) or isinstance(engDataToPyData(value), float)): 
                print(error("1.5", lineno))
                lineno += 1
                continue
            else:
                valuePy = engDataToPyData(value)

            if not ((f"add {value} to \'" in line or f"subtract {value} from \'" in line) and line.endswith("\'")):
                print(error("1.1", lineno))
                lineno += 1
                continue

            variable = noIndent(line).replace(f"add {value} to \'", "").replace(f"subtract {value} from \'", "")[:-1]
            
            if not variable in variables.keys():
                print(error("1.4", lineno).replace("<variable>", variable))
                lineno += 1
                continue
            if mode == "add":
                variables[variable] = variables[variable] + valuePy
            elif mode == "subtract":
                variables[variable] = variables[variable] - valuePy


        #repeat
        elif noIndent(line).startswith("repeat"): 
            repeats = noIndent(line).replace("repeat ", "").replace(" times:", "")
            if engDataToPyData(repeats) == TypeError:
                print(error("1.3", lineno))
                lineno += 1
                continue
            elif not isinstance(engDataToPyData(repeats), int): 
                print(error("1.5", lineno))
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
            code = noIndent(line).replace("throw error ", "")
            print(error(code, lineno))

        #not recognised
        else:
            print(error("1.0", lineno).replace("<command>", noIndent(line)))
        
        lineno += 1

