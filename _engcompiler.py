import colorama
import re

def error(code, line):
    errors = {
        "0.0": "Invalid error code: <invalidCode>",
        "0.1": "<fileName> is not an .eng file",
        "0.2": "Internal compiler code error:\n<error>",
        "1.0": "Command not recognised: \"<command>\"",
        "1.1": "No variable name specified",
        "1.2": "No variable content specified",
        "1.3": "Unknown data type",
        "1.4": "Unknown variable \"<variable>\""
    }

    if not code in errors.keys():
        error = errors["0.0"].replace("<invalidCode>", code)
        return colorama.Fore.RED + f"eng error 0.0 on Line {str(line+1)}: {error}" + colorama.Style.RESET_ALL
        return

    return colorama.Fore.RED + f"eng error {code} on Line {str(line+1)}: {errors[code]}" + colorama.Style.RESET_ALL

def compiler(file):
    f = open(file, "r").read().split("\n")
    variables = {}

    for line in f:
        for i in range(0, len(variables)):
            name = list(variables.keys())[i]
            value = variables[name]
            before = line
            varFuncStart1 = f"let <{name}> be "
            varFuncStart2 = f"set <{name}> to "
            line = line.replace(varFuncStart1, "").replace(varFuncStart2, "")
            after = line
            line = line.replace(f"<{name}>", str(value))
            if before != after:
                line = varFuncStart1 + line
        if re.search("let <(.*)> be ", line) == None and re.search("(?<=<)(.*)(?=>)", line) != None:
            print(error("1.4", f.index(line)).replace("<variable>", re.search("(?<=<)(.*)(?=>)", line).group(0)))
        
        #comments
        if line.strip() == "" or line.startswith("note:"):
            continue

        #print
        elif line.startswith("say \""):
            printed = line.strip().replace("say \"", "")[:-1]
            print(printed)

        #variables
        elif line.startswith("let"):
            if re.search("(?<=<)(.*)(?=>)", line) == None:
                print(error("1.1", f.index(line)))
                continue
            varName = re.search("(?<=<)(.*)(?=>)", line).group(0)
            
            rest = line.replace(f"let <{varName}> be ", "").strip()
            if rest == line:
                print(error("1.2", f.index(line)))
                continue

            if rest[0] == "\"" and rest[-1] == "\"": #string
                variables[varName] = rest[1:-1]
            elif rest.isdecimal(): #integer
                variables[varName] = int(rest)
            elif rest.split(".")[0].isdecimal() and rest.split(".")[1].isdecimal(): #float
                variables[varName] = float(rest)
            else:
                print(error("1.3", f.index(line)))
        else:
            print(error("1.0", f.index(line)).replace("<command>", line))