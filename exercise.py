#===================================================================
#    Purpose:   Demonstrate importing modules
#===================================================================

# Helper function that returns the number of vowels
def NumberOfVowels(stringValue):
    count=0
    for value in stringValue:
        if value in ['a','e','i','o','u']:
            count=count+1
    return count

# Helper to capitalize every other letter of a string
def CapitalizeHelper(stringValue):
    result = ""
    currentCapital = True

    for value in stringValue:
        if (currentCapital):
            result += str(value).upper()
            currentCapital = False
        else:
            result += str(value).lower()
            currentCapital = True
    return result

# Function to sort word list by length ascending
def SortByIncreasingLength(listOfWords):
    return sorted(listOfWords, key=len)

# Function to sort word list by length decending
def SortByDecreasingLength(listOfWords):
    return sorted(listOfWords, key=len, reverse=True)

# Function to sort word list by most vowels
def SortByTheMostVowels(listOfWords):
    return sorted(listOfWords, key=NumberOfVowels, reverse=True)

# Function to sort word list by leaset vowels
def SortByTheLeastVowels(listOfWords):
    return sorted(listOfWords, key=NumberOfVowels)

# Function to sort word list by capitalizing every other character
def CapitalizeEveryOtherCharacter(listOfWords):   
    result = []

    for value in listOfWords:
        result.append(CapitalizeHelper(value))

    return result

# Function to sort word list by reversing the order
def ReverseWordOrdering(listOfWords):
    result = listOfWords.copy()
    result.reverse()
    return result

# Function to sort word lis1t by folding words on middle of list
def FoldWordsOnMiddleOfList(listOfWords):
    result  = []
    length  = len(listOfWords)
    isOdd   = length % 2

    middleIndex = int(length / 2) + isOdd

    firstHalf   = listOfWords[:middleIndex]
    secondHalf  = listOfWords[middleIndex:]

    result.extend(secondHalf)
    result.extend(firstHalf)

    return result

# Function to display the contents of a word list
def DisplayList(listToDisplay, title):
    print(title)
    for value in listToDisplay:
        print (value)
    print()

# Main function
def main():
    
    continueProcessing = 0
    continueAddingWords = 0
    listOfWords = []

    # Main loop for program
    while True:
        continueProcessing = int(input("Process list of strings? Enter 1 for Yes or 2 for No: "))

        # Validate user input is 1 or 2
        if (continueProcessing != 1 and continueProcessing != 2):
            continueProcessing = int(input("Please enter 1 for Yes or 2 for No: "))
        elif (continueProcessing == 2):
            break
        else:
            # Loop to enter more words
            while (continueAddingWords != 2):
                continueAddingWords = int(input("Add another word? Enter 1 for Yes or 2 for No: "))
                # Validate input is 1 or 2
                if (continueAddingWords != 1 and continueAddingWords != 2):
                    continueAddingWords = int(input("Please enter 1 for Yes or 2 for No: "))
                else:
                    if (continueAddingWords == 2 and len(listOfWords) < 8):
                        print("Minimum of 8 words are required for each list.")
                        continueAddingWords = 1
                    elif (continueAddingWords == 1):                    
                        newWord = input("Please enter a word for the list: ")                    
                        listOfWords.append(newWord)

            # Call all functions for list
            sortByIncreasingLengthResult        = SortByIncreasingLength(listOfWords)
            sortByDecreasingLengthResult        = SortByDecreasingLength(listOfWords)
            sortByTheMostVowelsResult           = SortByTheMostVowels(listOfWords)
            sortByTheLeastVowelsResult          = SortByTheLeastVowels(listOfWords)
            capitalizeEveryOtherCharacterResult = CapitalizeEveryOtherCharacter(listOfWords)
            reverseWordOrderingResult           = ReverseWordOrdering(listOfWords)
            foldWordsOnMiddleOfListResult       = FoldWordsOnMiddleOfList(listOfWords)

            # Display all results for list
            DisplayList(sortByIncreasingLengthResult, "SortByIncreasingLength")
            DisplayList(sortByDecreasingLengthResult, "SortByDecreasingLength")
            DisplayList(sortByTheMostVowelsResult, "SortByTheMostVowels")
            DisplayList(sortByTheLeastVowelsResult, "SortByTheLeastVowels")
            DisplayList(capitalizeEveryOtherCharacterResult, "CapitalizeEveryOtherCharacter")
            DisplayList(reverseWordOrderingResult, "ReverseWordOrdering")
            DisplayList(foldWordsOnMiddleOfListResult, "FoldWordsOnMiddleOfList")

main()