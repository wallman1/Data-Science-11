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
March 5th

Today I created the correct project files and set up the initial architecture for the application. I set up the basic functionality for interacting with the API, which will set the stage for continuing further development. This included setting up API calls and allowing the framework to support minimal retrieval of data. Next, I will begin to create the graphical user interface (GUI) with TKInter.

March 10th

I began working on implementing the GUI and how to construct basic elements like labels and buttons using TKInter. I was taught event handling and widget layout management so that I can create a working and user-friendly interface. At the next phase, I will increase the number of elements on the interface and render its look more refined.

March 11th

I switched to an object-oriented approach to building the TKInter application, which made it easier to maintain and expand the project. By creating classes and methods, I created a more structured framework that will make it easier to add future additions and updates. My focus now is on eliminating any bugs that have occurred and further developing the GUI's functionality.

March 17th

I spent time working on a bug in the API functions that caused unintended behavior when getting data. I also attempted to create custom TKInter widgets to improve the UI experience, such as custom buttons and more efficient layout managers. My next assignment is to incorporate text entry boxes into the program so that the user can input data into the program.

March 18th

Today, I was able to successfully implement the text entry boxes in the TKInter GUI so that users may input values. I also implemented the search spells feature through the API, which retrieves and shows relevant information based on user queries. This is a critical step towards enabling user interaction with the spellbook. The next step will be working towards implementing the actual spellbook feature.

March 19th

I added a text file-based spellbook to the project, providing an effortless way to save and load spells. I also modified the search spells function so that it can handle a greater range of user input, thus making it more flexible. This modification allows users to search for spells with various parameters. In the future, I will add a list spells function to display the results in an organized manner.

March 21st

I fix some of the most important bugs in the GUI, including its responsiveness and appearance. I have also added the list spells function, which shows and lists all available spells. The next task will be fixing the main issues in the code and ensuring everything works flawlessly.

March 22nd

Today I worked on some of the larger bugs in the app that were holding things up, namely in functionality and data flow. After those were resolved, I could get back to work on the list spells function. Most of the emphasis from now on will be redoing the display logic so that there can be a more user-friendly and flexible presentation of the list.

March 24th

I continued to work on the list spells function, preparing it to become an effortless part of the GUI. I also fixed some small outstanding issues involving widget interaction and data handling. The list spells function is now effectively ready to be implemented. The next thing of note is ensuring it appears properly in the GUI.

March 25th

I focused on making the list spells function display correctly in the GUI, with all of the spell details being neatly laid out. I also focused on fixing errors with the operation of the spellbook, namely adding, modifying, and saving spells. The next task will be to continue developing the list spells feature, with a focus on the user interface.

March 31st

I was able to add a scrolling feature to the list spells function, which made it more efficient and capable of handling large data. I also completed the update spellbook function, which now allows users to update their spellbook in real time, with changes being stored instantly. The next step will be to finish the application by cleaning up the code, making it more efficient, and enhancing the user interface.

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