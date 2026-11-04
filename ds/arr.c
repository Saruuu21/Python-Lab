#include<stdio.h>
int main()
{
int size;
printf("\n Enter the number of elements in an array");
scanf("%d",&size);
int arr[size];
printf("\n Enter the %d elements of an array",size);
for(int i=0;i<size;i++)
{
scanf("%d",&arr[i]);
}

int max_value=arr[0];
for(int i=1;i<size;i++) 
{
 if(arr[i]>max_value)
 {
 max_value = arr[i]; 
 }
}
printf("The maximum value in the array is: %d\n", max_value);
return 0;
}
