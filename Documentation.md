## Requirements Definition

### Functional Requirements

#### View Data:

- Users are to have easy access to the information about spells in D&D 5e including but not limited to their titles, levels, and descriptions.

#### Error Handling:

- The application must manage errors, including inputs that don’t match with expected results, and API errors, in a way that can be identified from the application.

#### User Interface:

- In terms of aesthetics, the UI requires that the user can easily carry out navigation on intuitive pathways while accessing functions including spell search and spellbook management, which are logically structured consonant with usability principles.

#### Data Access:

- The application must always use real-time data, without using static files as a source, directly sourcing spell data from the D&D 5e API.

#### Spell Stats Access:

- Users need to access information detailing spells through search by name.

#### Spellbook Management:

- Users are able to add to the personal spellbook that they own by adding spells to it, enabling them to view the content of the spellbook at any selected duration and refresh its content whenever they choose.

### Non-Functional Requirements

#### Aesthetic Interface:

- The user interface should not only be easy to use but also visually appealing along with containing consistent design elements which will help improve layout.

#### Persistence:

- Every action taken by the user such as adding spells must be recorded and retrieved during subsequent sessions, meaning the information must persist across interactions with the application.

#### GUI:

- The application must come along with a graphical user interface which should be constructed in Tkinter or any other relevant library.

#### Performance:
- Even with large databases of spells, the application must quickly and seamlessly conduct searches, add new spells, or access the spellbook.

## Pseudocode
function ListSpells  

    Sort == 0  

    loop while Sort ≠ 7  

        output How Would You Like To Sort The List?:
            - 1. Spell Level
            - 2. Alphabetical
            - 3. Range
            - 4. Saving
            - 5. Casting Time
            - 6. Unsorted
            - 7. Quit 

        input Sort  

        if Sort == 1 then  

            output List Sorted By Spell Level 

        else  

            if Sort == 2 then  

                output List Sorted Alphabetically 

            else  

                if Sort == 3 then  

                    output List Sorted By Range 

                else  

                    if Sort == 4 then  

                        output List Sorted By Saving Throw

                    else  

                        if Sort == 5 then  

                            output  List Sorted By Casting Time

                        else  

                            if Sort == 6 then  

                                output Unsorted List

                            else  

                                output Please Input A Valid Response

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

    Finish == 0  

    loop while Finish == 0  

        if  then  

            output SpellValues  

            output  

            input Inp  

            Fin == 0  

            loop while Fin == 0  

                if Inp == 1 then  

                    AddSpell()  

                    Fin == 1  

                else  

                    if Inp == 2 then  

                        Fin == 1  

                    else  

                        output Pleas Input A Number Between 1 And 2 

                    end if  

                end if  

            end loop  

            input Finish  

        else  

            output Please Input A Valid Spell Name 

        end if  

    end loop  

    Main()  

end function

  

function Main  

    output  

    Quit == 0  

    input Use  

    loop while Quit == 0  

        if Use == 1 then  

            SearchSpells()  

        else  

            if Use == 2 then  

                ListSpells()  

            else  

                if Use == 3 then  

                    AddSpells()  

                else  

                    if Use == 4 then  

                        ViewSpells()  

                    else  

                        if Use == 5 then  

                            Quit == 1  

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
### Main
![alt text for screen readers](/flow1.png "stuff")
### List Spells
![alt text](/Flow2.png)
### Search Spells
![alt text](/Flow3.png)

## Gantt Chart
![alt text](/Gantt.png) 

## Data Dictionary
| Variable    | Data Type | Format for display | Size in bites | Size for display | Description                             | Example                                                                                                                                            | Validation                                      |
| ----------- | --------- | ------------------ | ------------- | ---------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Level       | Integer   | Whole Number       | 2             | 1                | The level of the spell                  | 1                                                                                                                                                  | Must be a number between 0 and 5                |
| Name        | String    | Text               | 50            | 50               | The name of the spell                   | Fire Bolt                                                                                                                                          | Must be a valid spell name                      |
| Description | String    | Text               | 200           | 200              | The description of the use of the spell | A bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame. | Must be a valid string that describes the spell |

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

## Maintainance
### Monitoring Changes to the API
As API alters, one needs to watch out for any new changes regarding the endpoints and any new parameters or response formats in the monitored API. To ensure sustained endurance, always opt for stable versions of the API. Balance the use of try-except blocks to gracefully manage errors, which can stem from the API or response modifications. Use try-except blocks of sufficient robustness to manage anticipative changes like errors from the API or response structure changes. api diagnosed issues with logging which aids keeping track of changes or lost requests. Along with that consider having secondary APIs set in place to prevent facing dead endpoints.

### Compatibility with Python and Libraries
Virtual environments are indispensable tools in managing a project’s dependencies, ensuring there are no conflicting requirements across multiple projects. Also checking if the requests and matplotlib have been updated and refresh them. Use the latest release of python and regularly check for any new publications to maintain compatibility across new releases for the program.

### After Deployement Fixing Bugs
When fixing a bug after deployment, I need to first replicate the issue by reproducing the conditions under which the error occurred. Use debugging tools, such as pdb, to trace the problem and pinpoint the exact cause. Once identified, implement the necessary fix and test it thoroughly to ensure the bug is resolved and no new issues are introduced. After testing, deploy the updated version and continue to monitor the program for any further issues.

## Peer Evaluation
### Person 1 - Miles
The program was very cool, The list of spells was very helpful because otherwise, I would be completely lost. The description of the spells was helpful, and layed out in a way that made very much sense. The spells storing over between sessions was a cool add on. Overall 11/10
### Person 2 - Viv
This program completed all the requirements of a fucntional API system, clearly displaying all the information needed. The GUI showed all the functions available and was very awesome. The code responded to incorrect code inputs and stored speels neatly. The system being able to save past information after being closed is a very useful and impressive fucntion that improves the user's experience. This sytem was very well coded and every function was completed with great planning and implementation. 11/10

## Final Evaluation
The application meets the operational needs of displaying spell details, handling a spellbook, and interacting through a user-friendly interface for D&D 5e spells. There is reasonable usability of the application; however, it could be improved by better error management, design, and overall speed of execution. Also, the handling of files and validation of user data could be improved to make sure user information is consistent throughout sessions. The system's architectural style along with its code comments are accurate, but the application’s functionality and overall user experience would benefit from more refined interface and user interaction design alongside additional sophisticated usability features.