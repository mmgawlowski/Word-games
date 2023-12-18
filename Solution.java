import java.util.*;
import java.util.stream.Collectors;

/**
 Two strings are anagrams if they have the same characters in the same frequency, but the characters are in a different order. An example
 is bat and tab.

 Given a collection of strings, group the anagrams and return the number of groups formed.

 Example

 words = ["cat", "listen", "silent", "kitten", "salient"]

 Only silent and listen are anagrams. The last word, salient, contains an extra 'a'. No other words are anagrams, so there are 4 groups: [
 ['silent', 'listen'], ['cat'], ['kitten'], ['salient']]. Return 4.

 Function Description

 Complete the function getGroupedAnagrams in the editor below.

 getGroupedAnagrams has the following parameter(s):
 string words[n]: an array of strings

 Returns
 List<List<String>>: the groups formed

 Constraints

 1 <= n <= 104
 1 <= length of words[i] <= 50
 words[i] consists of lowercase English characters only.
 */
public class Solution {
    public static List<List<String>> getGroupedAnagrams(String[] words) {
        if (words.length < 1 || words.length > 104) {
            throw new IllegalArgumentException("The 'words' array should contain from 1 to 104 elements.");
        }

        if (Arrays.stream(words).anyMatch(w -> w.isEmpty() || w.length() > 50 || w.matches(".*[^a-z].*"))) {
            String notAllowedWords = Arrays.stream(words)
                                           .filter(w -> w.isEmpty() || w.length() > 50 || w.matches(".*[^a-z].*"))
                                           .collect(Collectors.joining("\",\"", "\"", "\""));

            throw new IllegalArgumentException("A word can only contain lowercase letters of" +
                " the English alphabet and its length must be between one and 50 letters.\n" +
                "These words don't comply with mentioned rules: " + notAllowedWords);
        }

        Map<String, List<String>> anagramsMap = new HashMap<>();
        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            if (!anagramsMap.containsKey(key)) {
                anagramsMap.put(key, new ArrayList<>());
            }
            anagramsMap
                .get(key)
                .add(word);
        }
        List<List<String>> groupsList = new ArrayList<>(anagramsMap.values());
        System.out.println("The number of formed groups: " + groupsList.size());
        return groupsList;
    }

    public static void main(String[] args) {
        String[] words = {"pineapple", "", "restful", "cheater", "teacher", "santa", "fluster", "antas"};
        System.out.print(getGroupedAnagrams(words));
    }
}
