int lengthOfLongestSubstring(char * s){
       int len = strlen(s);
    int ans = 1;
    if(len == 0){
        ans = 0;
    }
//    for (int win_left = 0;win_left <= len;win_left++){
//        for (int win_right = 0; win_right > win_left; win_right--){
//            for (int check_1 = win_left; check_1 <= win_left; win_left++){
//                for (int check_2 = win_right; check_2 > check_1; check_2--){
//                    if (check_1 == check_2){
//                        break;

    int win_left, win_right;
    int  end_point;
    int have_ans = 0;
    for (win_left = 0; win_left< len; win_left++){
        end_point = 0;
        win_right = win_left + 1;
        while (end_point == 0 && win_right <= len){
            for (int check_1 = win_left; check_1 < win_right; check_1 ++){
                if (s[check_1] == s[win_right]|| win_right == len){
                    have_ans = 1;
                    int temp_ans = win_right - win_left;
                    if (temp_ans > ans){
                        ans = temp_ans;
                    }
                    end_point = 1;
                    break;

                }
            }
            win_right ++;
        }
    }
    if (have_ans == 0){
        ans = len;
    }
    return ans;

}