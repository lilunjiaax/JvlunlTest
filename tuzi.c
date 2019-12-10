/*
赛码网C语言标准输入输出
*/
#include <stdio.h>
int main()
{
   int N, M;
    // 每组第一行是2个整数，N和M，至于为啥用while，因为是多组。
   while(scanf("%d %d", &N, &M) != EOF) {
      printf("%d %d\n", N, M);
      // 循环读取“接下来的M行”
      for (int i=0; i<M; i++) {
        int a, b, c;
        // 每行是3个整数，a，b，c。
        scanf("%d %d %d", &a, &b, &c);
        printf("%d %d %d\n", a, b, c);
      }
      // M行读取完了，就又要开始下一组了，去while那里。
   }
}

