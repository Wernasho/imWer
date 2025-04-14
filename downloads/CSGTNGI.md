Just to make sure you're in the right place, this is a C guide. Not C++, Not C#. C. Raw, weird and senseless C.

When it comes to headers, C compiler is an iPad kid and the headers are the iPad. Dare to separate them and your code will be as useful as a microphone for a mute.

#include <stdio.h>   -> For printf(), scanf()  
#include <stdbool.h> -> For bool (Why the hell do you need to INCLUDE something as basic as booleans????) 
#include <stdlib.h>  -> For malloc(), free(), exit()  
#include <string.h>  -> For strcpy(), strlen() 
#include <math.h>    -> For math functions (sqrt(), pow(), powf(), etc.) 

apparently, const is used to notate that a variable is immutable.

fn == function // Update: This doesn't exist and if you use it C will think you're a Russian Rust spy
void == function that doesn't return anything

Apparently strings, or "chars" are 'pointers' and need a * at the end:

char* message = "What in everything holy is a pointer. Send Help";

And strings can also be "character arrays"???

char plea_for_help[] = "what the hell is wrong with C"; 

Okay, so, the `void funcName() {}` thingy wasn't just to make me miserable. It's actually part of the syntax. `int funcName() {}` returns... You guessed it, an int. That makes sense

variable format:

const: well what else could this keyword possibly do

const char* varName= "hi";

bool boolean = false; //needs #include <stdbool>

int varName = 346;

const char best_greek_letter = 'Σ';

char alpha = 'α'; //This is a character

char* alpha2 = "άλφα" //And THIS IS A STRING??? ONE CHARACTER OF DIFFERENCE?????

char alhphaSquared[] = "ΆΛΦΑ" //And this is also a string... What the hell C...

float pi = 3.14; // "Idgaf about anything" type of decimal

double π = 3.141592653589793; // "Give me precision or I'll die" type of decimal

... Why in the holy fuck is 'char' used for both strings and single characters.

Oh yeah and uhh `printf()` == `print!()`

I hate my life, so, placeholders:


|placeholder | meaning                        |
|------------|--------------------------------|
|    %d      | integer                        |
|    %s      | string                         |
|    %f      | float                          |
|    %.2f    | float(2 decimals)              |
|    \n      | new line (obviously)           |
|    %%      | literally %                    |
|    %c      | single character               |
|    %lf     | double (for scanf(); only)     |
|    %p      | Pointer                        |
-----------------------------------------------

Let's say you're making a function that prints a message:

```c
#include <stdlib.h>


void print_message(char* message) {
    printf(message);
}

```


May god have mercy on you if you dare to do that. Remember: C is a cult and the annoying placeholders are its god. If you don't worship them C will get mad at you. And even if you did use placeholders your compiler would still yell at you because you're returning nothing inside of an int function. 
Legal way to do this:


```c
#include <stdlib.h>


int print_message(char* message) {
    printf("%s" ,message);
    return 0;
}

int main() {
    print_message("nothing makes sense in C");
    return 0;
}

```

If you see `error: expected ‘;’ before ‘}’` , you forgot a semicolon. Again. And the compiler will yell at you.

Existencial crisis: does this code work?

```c

#include <stdlib.h>

int main() {
    int i = 0;
    i++;
    printf("%d", i); //this SHOULD output 1 (it does)
    return 0;
}

```


Oh and by the way, remember: printf() is NOT your usual print().
This is not your fancy Python or Rust. No. This is Raw C.


```python

num = 987

print(num)

```


You think that this works in C?


```c
#include <stdlib.h>

int num = 987;

printf(num); //The compiler yells at you (and it should).

```

Of course it doesn't. Remember: 'C is a cult and the annoying placeholders are its god. If you don't worship them C will get mad at you.'

This is the way to do it:

```c
#include <stdlib.h>

int num = 987;

printf("%d", num); //C compiler gods are pleased 

```


And also, "%d" is selfish. "%d" makes everything about itself (literally)


```c
#include <stdlib.h>

int main() {
  printf("%d", 5 / 4);
  return 0;
}

```


This SHOULD output a decimal. But NOO, Remember kiddo, this is C. You don't have your fancy dynamic tyiping in here.
If you ask for a int, you get int. And yes, printf("%d", 5 / 4) outputs 1. C logic you mere high-levels wouldn't comprehend.
So you'd think that "%f" would do the same.
Kid,
This is C.
the words "Sense", "coherence" and "accuracy" are unknown to C.


```c
#include <stdlib.h>

int main() {
  printf("%f", 3);
  return 0;
}

```


You guessed it, it outputs to 3. yes 3. Not 3.0. 3. (Don't try this at home, your compiler will run the code but it will be disappointed) 

but this:


```c

#include <stdlib.h>

int main() {
  printf("%f", 3.0);
  return 0;
}

```


Outputs 3.000000 because C turns it into a double, not a float.

OKAY.

Enough whining. 

Let's talk about something useful.


In C, we're practically cavemen, we haven't discovered things like "**" yet. We use pow(num, exponent)


```c 
#include <stdlib.h>
#include <math.h>

int main() {
  printf("%f", pow(2, 5)); //(2 * 2 *2 * 2 * 2 =  32)
  return 0;
}

```


And for some reason unbeknown to me, pow() returns a double, so you have to use "%f".

Now, yes, every language has an exponentiation feature. But you know what most don't? Square roots.


```c
#include <stdlib.h>
#include <math.h>

int main() {
  
  printf("%f", sqrt(64));
  return 0;
}

```


And then we have ceil() which rounds a double/float to the next integer. 


```c
#include <stdlib.h>
#include <math.h>

int main() {
  
  printf("%f", ceil(3.14549)); //4
  return 0;
}

```


and floor() is ceil()'s evil twin. It rounds the number down


```c
#include <stdlib.h>
#include <math.h>

int main() {
  
  printf("%f", floor(3.14549)); //3
  return 0;
}

```


C's scanf() is Python's input()'s older brother. It literally does the same.
So, yes, technically `input()` == `scanf()`.

Actually useful example with scanf():

Let's say you want the user to input their age. You do it this way:


```c
#include <stdlib.h>


int main() {
    int age;
    printf("Enter your age");
    scanf("%d", &age); 
}

```

`int age;` declares the variable but does not assign a valuue
`scanf("%d", &age)` tells C that we want to store an integer inside of the `age` variable.
And yes, &age is a pointer. We're getting into the danger zone. What is a poiner? I don't know and I don't want to know.

Oh, and remember the `char plea_for_help[]` being a string? Well the [] aren't decorations, apparently we can smash a number in there and that will tell C
"Hey. This string can only have x characters"
And if you go over that limit the compiler implodes.

```c
#include <stdio.h>


int main() {
    char name[20];
    printf("Enter your name");
    scanf("%s", name); 
}

```
Oh, yes. C being C. You don't need that black magic called "pointers" for strings... For some reason. 

Anwyay,

So, apparently when using scanf() it completely ignores everything after the first space. So in the code above if you enter something like, idk, "Mike Weber" it's only going to store "Mike". Just another beautiful, perfectly logical C quirk, like every other quirk. But hey, at least you can be proud of using C instead of boring, basic high-level languages like shitscript or "Python". Nah, using C makes you more manly.

Oh yeah we have to use fgets(); in order to get a string with spaces. Sounds nice to me.
fgets format: fgets(variable, character limit, stdin); stdin stands for STanDard INput. It's bascially just getting the text from the console or something, idk.
Oh, and fgets wants to make us miserable because it adds a newline after the input like the little rebel it is.

OKAYYYY ARRAY TIME YIPPIEEEE

Array secret formula:

type this_is_an_array[amount of items your array can hold] = {..., ..., ...};

E X A M P L E :

char greek_letters_lowercase[24] = {'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 
  'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'σ', 'ς', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω'};


wait. I just noticed something
Text in programming is called 'string' because they are a STRING of consecutive characters... That makes sense now. 

Okay so, switch statements
switch statements are basically a debuff of if statementes. They check one variable against some different values

```c
#include <stdio.h>

int main() {
    char name[4] = "Mike";
    switch(name)
    {
        case "Mike":
            printf("Very sigma");
        case "John":
            printf("Still sigma (but not as much)");
        case "Mia":
            printf("Wrong gender bud");
        default:
            printf("Not sigma");
    }
}

```

 o  k  a  y  so apparently "Objects" or "dictionaries" in C are called "Structs"... And they're also outside of the main function. Nice.

```c

struct Person 
{
    char name[8] = "Wernasho";
    int age = 13;
    char occupation[4] = "None";
}

strcut Person person1;

```


That last thing right there made a another struct with the same properties as Person. Basically like an instance of a class. And how can we modify that shyt? Well, easy:


```c

person1.age = 26;
printf("%d", person1.age); //26


```


"Oh, cool, so then person1.name = "sflkjhsadlgjkhsd" should also change the name, right?" HAha NO. This is C. Nothing makes sense here. You have to use strcpy() to do that.


```c

strcpy( person1.name, "Joe");
printf("%s", person1.name); //Joe

```

Remember that I said "Basically like an instance of a class"? The course guy literally said "Kinda like an INSANCE of that struct" so yeah. We've been lied to. C does have OOP (sorta)

o    k    a    y
it's time for 2D arrays, hooray!
in C-mple terms: 
2D array == array where all arrays are arrays
Okay so when you declare a 2d array you have to add two square brackes (type arrayName[arrays inside the first array][elements inside the arrays];)

example of a 2d array:

int greekLetters[][] = {
  {'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'σ', 'ς', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω'},
  {'Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Σ', 'ς', 'Τ', 'Υ', 'Χ', 'Ψ', 'Ω'}
}

okay so apparently you can declare several variables at once, like
int your, mother;

Variables, data and all that shit is stored inside of an addres in your physical Random Access Memory (RAM) in your PC. You can access said "addres" with printf("%p", &variable)

Wait what the fuck do you mean you can store pointers in "pointer variables" 😨
Oh nvm it's actually easy
So basically pointer variables store the memory address of certain variable, like:

```c

int main()
{
  char sigma 'Σ';
  char * sigmaAdress = &sigma; //stores the memory adress of sigma variable
}

```

okay so uhhh you can make and edit files with C which is really nice. 
Wait... I just called a C feature nice... I never thought this moment would come.

```c

int main()
{
  FILE * varName = fopen("filename.extension", "mode");
  fprintf("file content"); //changes the file's content
  fclose(varName); //closes the file because this ain't Python and no one does nothing for you
}


```


fopen modes: 

|mode | meaning| what it does |
|-----------------------------|
|"w"| write | REPLACES current content|
|"a"| Append | ADDS to the current content|
|"r"| Read | er... Shows stuff, I guess? Don't really know how to explain this one|
-------------------------------


So, let's say that I want to make a file called test.bzm and store "Hi, hello. This is a test." inside of it. This is how I'd do it:

```c

int main()
{
  FILE * fileTest = fopen("test.txt", "w");
  fprintf("Hi, hello. This is a test.");
  flcose(fileTest);
}

```

Voilà. We just made a file, hurray!