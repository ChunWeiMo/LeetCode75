#include <string>
#include <iostream>

using namespace std;

/**
 * Merges two strings alternately character by character.
 
 * @param word1 The first string to merge.
 * @param word2 The second string to merge.
 * @return The merged string with alternating characters from `word1` and `word2`.
 */
string mergeAlternately(string word1, string word2)
{
    string merge_string;
    int position_1 = 0;
    int position_2 = 0;

    merge_string = "";
    while (position_1 < word1.length() || position_2 < word2.length())
    {
        if (position_1 == word1.length())
        {
            merge_string += word2.substr(position_2);
            break;
        }
        else if (position_2 == word2.length())
        {
            merge_string += word1.substr(position_1);
            break;
        }
        else if (position_1 <= position_2)
        {
            merge_string += word1.substr(position_1, 1);
            position_1++;
        }
        else
        {
            merge_string += word2.substr(position_2, 1);
            position_2++;
        }
    }

    return merge_string;
}

int main()
{
    cout<<mergeAlternately("abc","pqr")<<endl;
    cout<<mergeAlternately("ab","pqrs")<<endl;
    cout<<mergeAlternately("abcd","pq")<<endl;
    return 0;
}
