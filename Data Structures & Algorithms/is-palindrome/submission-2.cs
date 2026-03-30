public class Solution {
    public bool IsPalindrome(string s) {
        // wasitacaroracatisaw
        //  tab a cat --> tabacat 

        //s = tab a cat. 


        int i = 0;
        int j = s.Length -1;
        string validCharacters = "abcdefghijklmnopqrstuvwxyz1234567890";

        while( j > i){
            // in the case that its a valid character acccept it, otherwise go to next
            while(!char.IsLetterOrDigit(s[i]) && i < s.Length - 1){
                i++;
            }
            while(!char.IsLetterOrDigit(s[j])  && j > 0){
                j--;
            }


            if(j < i)
                return true;
Console.WriteLine("Comapred " + s[i] + " and " + s[j]);

            if(Char.ToLower(s[i]) != Char.ToLower(s[j])){
                Console.WriteLine("happened at " + i + " " + j);
                
                return false;
            }



            i++;
            j--;
        }

        return true;
    }
}
