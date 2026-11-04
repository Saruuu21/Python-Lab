#include<stdio.h>
int main()
{
int s1,s2,s3,a1[10],a2[10],a3[20],i,j,k;
printf("\n Enter the number of elements in 1st array:");
scanf("%d",&s1);
printf("\n Enter the %d elements of an array",s1);
for(int i=0;i<s1;i++)
{
scanf("%d",&a1[i]);
}
printf("\n Enter the number of elements in 2nd array:");
scanf("%d",&s2);
printf("\n Enter the %d elements of an array",s2);
for(int i=0;i<s2;i++)
{
scanf("%d",&a2[i]);
}
s3=s1+s2;
i=j=k=0;
while(i<s1 && j<s2)
{
if(a1[i]<a2[j])
{
a3[k]=a1[i];
i++;
}
else
{
a3[k]=a2[j];
j++;
}
k++;
}
while(i<s1)
{
a3[k]=a1[i];
i++;
k++;
}
while(j<s2)
{
a3[k]=a2[j];
j++;
k++;
}
printf("\n Merged Array is:\n");
for(i=0;i<s3;i++)
printf("%d",a3[i]);
printf("\n");
return 0;
}
