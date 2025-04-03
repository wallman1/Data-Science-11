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

