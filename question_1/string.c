#include <stdio.h>
#include <ctype.h>

int main() {
    char str[101];
    int i, charCount = 0, alphabetCount = 0, vowelCount = 0, consonantCount = 0, digitCount = 0, wordCount = 0, specialCount = 0;
    char ch;

    printf("Enter a string (max 100 characters): ");
    fgets(str, sizeof(str), stdin);

    for (i = 0; str[i] != '\0'; i++) {
        ch = str[i];
        if (ch != '\n') {
            charCount++;
        }
        if (isalpha(ch)) {
            alphabetCount++;

            if (tolower(ch) == 'a' || tolower(ch) == 'e' || tolower(ch) == 'i' || tolower(ch) == 'o' || tolower(ch) == 'u') {
                vowelCount++;
            } else { 
                consonantCount++;
            }
        } else if (isdigit(ch)) {
            digitCount++;
        } else if (ch == ' ' || ch == '\t' || ch == '\n') {
            wordCount++;
        } else {
            specialCount++;
        }
    }
    if (charCount > 0) {
        wordCount++;
    }

    printf("\nNumber of characters: %d\n", charCount);
    printf("Number of alphabets: %d\n", alphabetCount);
    printf("Number of vowels: %d\n", vowelCount);
    printf("Number of consonants: %d\n", consonantCount);
    printf("Number of digits: %d\n", digitCount);
    printf("Number of words: %d\n", wordCount);
    printf("Number of special symbols: %d\n", specialCount);

    return 0;
}
