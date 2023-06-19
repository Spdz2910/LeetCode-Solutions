public class Solution {
    public IList<string> LetterCombinations(string digits) {
        if(string.IsNullOrEmpty(digits))
            return new List<string>();
        string[] mapping = new string[]
        {
            "",     // 0
            "",     // 1
            "abc",  // 2
            "def",  // 3
            "ghi",  // 4
            "jkl",  // 5
            "mno",  // 6
            "pqrs", // 7
            "tuv",  // 8
            "wxyz"  // 9
        };

        IList<string> combinations = new List<string>();
        GenerateCombinations(digits, mapping, combinations, "", 0);
        return combinations;
    }
    
    private void GenerateCombinations(string digits, string[] mapping, IList<string> combinations, string current, int index)
    {
        if(index == digits.Length)
        {
            combinations.Add(current);
            return;
        }
        char digit = digits[index];
        string letters = mapping[digit -'0'];
        for(int i = 0; i < letters.Length; i++)
        {
            GenerateCombinations(digits, mapping, combinations, current + letters[i], index+1);
        }
    }
}
