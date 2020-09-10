# Sajilo Programming Language Final Alpha Version :smiley:

This is the final alpha version of Sajilo. 

#### ‘Sajilo Programming Language’ is a basic programming language compiler written in Python and PLY. It offers Romanized Nepali syntax for the ease of use to the Nepali speakers.  

![English Logo](screenshots/englogo.png)

![Nepali Logo](screenshots/np_logo.png)

## Requirements
:one: PLY (Python Lex and Yacc)

:two: Regex

## How to Run
:one: Download or clone the files from repo.
```git clone https://github.com/parz3val/sajilo-alpha```

:two: Change into the directory and install the requirements.
```pip install -r requirements.txt```

:three: Run the sajilo code with `sajilo.py` file.
Usage : ```python sajilo.py 'name of file'```

>> For example run:
``` python sajilo.py examples/sansaar.sajilo```


## Features
:one: Basic math operations

:two: User defined variables

:three: User defined functions

:four: Function Calls

:five: Standalone functions and no class overhead.

:six: LR Parsing


## Activities
:white_check_mark: Basic Lexer

:white_check_mark: Parser and Interpreter

:white_check_mark: Lexing Error fixed for the conjoined syntax.

:white_check_mark: Solve the lexing error with the joined key instances.

:white_check_mark: Solved index out of range error in yacc file.

>> For example :
```lekha "hello World"  is parsed correctly but,
lekhasss "Hello World" is also parsed as right syntax
This issue is solved now!
```



## User Guide and Syntax


#### A Simple Hello World Program
``` lekha "Hello World" ;``` 

>> The more sophisticated way to do this would be with user defined functions.

```

// This program takes input from user and returns message
// Functions are declared with keyword vidhi
// Functions don't have side affects, meaning they don't change the supplied value.
// They can be called with/without arguments

vidhi namaste(naam) {
    lekha "Namaste, ", naam, "\n";
}

naam = padha("Hello, tapaiko naam k ho? \n");
namaste(naam);

```
1. Statements are ended in semicolon.

#### Variables
Sajilo has dynamic types for the ease of use. Meaning you can define variables by assigning values to them.
Sajilo supports all major data types like integers, floats, strings, and boolean values.

#### Integers (अंक)
To type cast from string to integers or floats to integer. Use the function `anka`
>> For example

```
a = padha("Enter one number: ")
// a is casted from string to integer if possible.
// Error is raised if not.
a = anka(a);
```

#### Floats (दशमलब) - > dash
To type cast from integers to floats or strings to floats (is possible.)
Use function `dash`
```
a = 5;
a = dash(a);
// a will be 5.0
```

#### Strings (अक्षर)
To type cast from integers/floats/ or other objects to strings use functions `sabda`

```
a = 5;
a = sabda(a);
// a will be "a" 
```

#### Bolean Values (True/False)
We can declare true and false for boolean values. I didn't translate the type to Nepali as a respect to George Boole.
```
a = true
```

#### Conditionals 
Sajilo supports basic comparison between values and varialbes with operators and conditions.
Supported conditionals are 'YEDI', 'NAVAYE', 'NAVAYE YEDI'

#### ```यदी / नभये ```

```
a = 5;
yedi a % 2 == 0 {
    lekha "Even\n";
}
navaye {
    lekha "Odd\n";
}
```
### 4. Loops 
Sajilo supports loops and control flow with `loop` (functions similar to for loop.) and `jaba` (functions similar to while loop)

#### ``` लूप/जब ```

```
// A program to print numbers from 1 to 10.
i = 0;
loop i lai 1 -> 10 {
    lekha i;
    lekha "\n";
}
```

#### ``` जब ```
```
ans = "y";

jaba ans == "y" {
    user_input = padha("Enter one number: \n");

    yedi user_input == "n" {
        ans = user_input;
    }

    sankhya = anka(user_input);
    
    yedi sankhya < 0 {
        lekha "Negative number";
    }
    navaye {
        lekha "Positive Number";
    }

```

### 4. Functions / Methods (विधी /vidhi)
Functions are treated as a small block of computations in Sajilo and and are declared with the keyword `vidhi`
Vidhi is Nepali means recepie for doing something, which is quite fitting name. 

```
// a method to tell if a number is odd or even//

ans = "y";

jaba ans == "y" {
    user_input = padha("\nEnter one number: \n");

    yedi user_input == "n" {
        ans = user_input;
    }

    sankhya = anka(user_input);
    
    yedi sankhya % 2 == 0 {
        lekha "Even number \n";
    }
    navaye {
        lekha "Odd Number";
		lekha "\n";
    }

}
```

## Known Issues and Bugs
:o: Unicode Transformations and encodings don't work.

## Contribution
Feel free to use and fork the repo as you wish. If you would like to participate in the project and translate the language keywords, error messages and programming style for your language or help me improve the code (there is also a private version of parsers being implemented in C and LLVM for code execution): feel free to open a PR request and I will add a branch for your language. All the code is subject to change however.


## References
>> Check docs/References.csv for complete list of References, tutorials, and books.
