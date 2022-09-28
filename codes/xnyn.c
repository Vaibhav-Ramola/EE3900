#include<stdio.h>
#include<stdlib.h>

int main(){
    
    FILE *fptr;

   // use appropriate location if you are using MacOS or Linux
   fptr = fopen("program.dat","w");

   if(fptr == NULL)
   {
      printf("Error!");   
      exit(1);             
   }

    int x[6] = {1,2,3,4,2,1};
    float y[20];

    y[0]= x[0];
    y[1] = -0.5*y[0] + x[1];
 
    for(unsigned int i=2; i<20; i++){
        if(i < 6){ 
            y[i] = -0.5*y[i-1] + x[i] + x[i-2];
        }

        else if(i >=6 && i<8){
            y[i] = -0.5*y[i-1] + x[i-2];
        }

        else y[i] = -0.5*y[i-1];

        //fprintf(fptr, "%lf ", y[i]);
    }
    
    
    for(unsigned int i=0; i<20; i++){ fprintf(fptr, "%lf ", y[i]);}
    fclose(fptr);
    return 0;
}