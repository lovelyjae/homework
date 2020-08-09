/*반복문 및 배열을 사용하는 프로그램 작성
100개의 정수 입력
최솟값, 최대값, 합, 평균, 평균값 이하의 갯수 출력
반복문, 배열에 대한 설명하기
*/


#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int i;
    int min, max, sum, avg, low_avg_count;
    int data[100]; 

    printf("100개의 정수를 입력하시오:\n ");
    for(i=0; i<100; i++)
    {
      scanf("%d", &data[i]);  
    }
    min=data[0]; 
    max=data[0];
    sum=0;
    low_avg_count=0;
    
    for(i=0; i<100; i++)
    {
      if(min>data[i])
      {
        min=data[i];
      } 
      if(max<data[i])
      {
        max=data[i];
      }
      sum=sum+data[i];
    }
     avg=sum/100;
    for(i=0; i<100;i++)
    {
      if(avg>=data[i])
      {
        low_avg_count++;
      }

    }

    printf("최솟값은%d이다\n",min);
    printf("최댓값은%d이다\n",max);
    printf("합은 %d이다\n",sum);   
    printf("평균은 %d이다\n", avg);
    printf("평균값 이하의 갯수는 %d이다\n",low_avg_count);

    return 0;
}
