#include<stdio.h>
int main()
{
int n,d=0,sum=0;
printf("\n Enter The number");
scanf("%d",&n);
while(n>0)
{
  d=n%10;
  sum=sum+d;
  n=n/10;
}
printf("sum of digit=%d",sum);
printf("\n");
return 0;
}
