## Requirements Definition

### Functional Requirements

- The project needs to be able to allow the user to view data  
- The project needs to handle errors and edge cases cleanly and properly  
- The project needs to have a user interface that is clear and concise  
- The project needs to access data without the loading of a csv file  
- The user needs to be able to access the stats of each spell

### Non-Functional Requirements

- The project should have an aesthetically pleasing interface  
- The project should save past interactions  
- The project should have a graphical user interface  
- The project should be able to run quickly and efficiently  
- The code should be devoid of any redundancies

## Pseudocode

function ListSpells  
    Sort \= 0  
    loop while Sort ≠ 7  
        output   
        input Sort  
        if Sort \= 1 then  
            output   
        else  
            if Sort \= 2 then  
                output   
            else  
                if Sort \= 3 then  
                    output   
                else  
                    if Sort \= 4 then  
                        output   
                    else  
                        if Sort \= 5 then  
                            output   
                        else  
                            if Sort \= 6 then  
                                output   
                            else  
                                output   
                            end if  
                        end if  
                    end if  
                end if  
            end if  
        end if  
    end loop  
    Main()  
end function

function SearchSpells (SpellName)  
    input SpellName  
    Finish \= 0  
    loop while Finish \= 0  
        if  then  
            output SpellValues  
            output   
            input Inp  
            Fin \= 0  
            loop while Fin \= 0  
                if Inp \= 1 then  
                    AddSpell()  
                    Fin \= 1  
                else  
                    if Inp \= 2 then  
                        Fin \= 1  
                    else  
                        output   
                    end if  
                end if  
            end loop  
            input Finish  
        else  
            output   
        end if  
    end loop  
    Main()  
end function

function Main  
    output   
    Quit \= 0  
    input Use  
    loop while Quit \= 0  
        if Use \= 1 then  
            SearchSpells()  
        else  
            if Use \= 2 then  
                ListSpells()  
            else  
                if Use \= 3 then  
                    AddSpells()  
                else  
                    if Use \= 4 then  
                        ViewSpells()  
                    else  
                        if Use \= 5 then  
                            Quit \= 1  
                        else  
                            input   
                        end if  
                    end if  
                end if  
            end if  
        end if  
    end loop  
    output   
end function

## Structure Chart
![alt text for screen readers](/Screenshot%202025-04-02%20091506.png "stuff")

## Flowcharts

## Commit Records
- March 5th
Today I created the nessecary files for the project and added the initial funtions for the api work. I will start work on devolping a GUI with TKInter next.

- March 10th
Worked on adding a GUI and learnt how to create labels and buttons with TKInter. I will continue work on the GUI next.

- March 11th
Worked on making a TKInter application with object oriented coding allowing for easier additions to the application. I will work on using tkinter and fixing bugs next.

- March 17th
Fixed bug within the api functions and experitmented with custom TKInter. I will work on using text entry boxes.

- March 18th
Worked on getting text entries impelmented, also implemented the search spells function using the api. I will work on adding the spellbook next.

- March 19th
Added the a txt file spellbook and changed the search spells function to encompass more use cases. I wil create a list spells function next.

- March 21st
I fixed a few of the bugs in the GUI and added the list spells function. I will finish debugging the main errors within the code next.

- March 22nd
I fixed many of the larger errors inside the code allowing for progress to continue. I will work on the list spells function to allow for a different display approach next.

- March 24
I worked on getting the list spells function ready for use within the GUI and fixed a few oustanding bugs. I will work on displaying the list spells function next.

- March 25th
I worked on getting the list spells function to display properly and worked on fixing the spellbook functions. I will continue working on the list spells function next.

- March 31st
I got the list spells function to scroll within the GUI and completed the update spellbook function to allow for real time updating of the spellbook. I will finish polishing the code next.
