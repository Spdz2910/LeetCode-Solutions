public class Solution {
    public string IntToRoman(int num) {
        //Cách 1
        //Dictionary<int,string>romanNumeral = new Dictionary<int, string>(){
        //    {1000,"M"},
        //    {900,"CM"},
        //    {500,"D"},
        //    {400,"CD"},
        //    {100,"C"},
        //    {90,"XC"},
        //    {50,"L"},
        //    {40,"XL"},
        //    {10,"X"},
        //    {9,"IX"},
        //    {5,"V"},
        //    {4,"IV"},
        //    {1,"I"},
        //};
        //string result ="";
        //foreach(var kvp in romanNumeral){
        //    while(num >= kvp.Key )
        //    {
        //        result += kvp.Value;
        //        num -=kvp.Key;
        //    }
        //}
        //return result;

        //Cách 2 : sử dụng mảng 2 chiều
        string[,]romanNumerals = new string [,]{
            {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"},
            {"1000", "900", "500", "400", "100", "90", "50", "40", "10", "9", "5", "4", "1"}
        };

        string result ="";
        int i = 0;
        while(num>0)
        {
            int value = int.Parse(romanNumerals[1,i]);
            string symbol = romanNumerals[0,i];

            if(num >= value)
            {
                result += symbol;
                num -= value;
            }
            else
            {
                i++;
            }
        }

        return result;
    }
}