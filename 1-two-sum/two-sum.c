/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
	int*array=(int*)malloc(sizeof(int)*2);
    for(int i=0;i<numsSize;i++){//直接多个for循环暴力破解
        for(int j =i+1;j<numsSize;j++){
            if(nums[i]+nums[j]==target){
                array[0]=i;
                array[1]=j;
                *returnSize=2;
                return array;
            }
        }
    }
     	*returnSize=0;
    	*array=NULL;
    	return array;
}  