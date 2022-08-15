#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define PI 3.141592

float ask();
float area(float r);
void print(float);

main()
{
      int dec, choice;
      float Vci, Vco, r,h, ar;

      do {
	printf("Hello.\n");
      printf("Do you want to calculate the volume of...? \n1) Cylinder \n2) Cone\n");
      scanf("%i", &dec);
      printf("Write the value of the radius\n");
      scanf("%f", &r);
      ar = area(r);
    
      if(dec == 1) {
        h = ask();
        Vci = ar * h;
        print(Vci);
      }
      else {
      h = ask();
    	Vco = (Vci) / 3;
      print(Vco);
	}   

      printf("Do you want to calculate another volume? \n1)Yes \n2)No\n");
      scanf("%i", &choice);

      }
	while (choice == 1);
      
	system("PAUSE");
      system("cls");
      printf("A La Gloria Del Gran Arquitecto Del Universo\n");
      system("PAUSE"); 
}

float ask()
{
      float h;     
      printf("Write the value of the height\n");
      scanf("%f", &h);
      return h;
}

float area(float r)
{
     float area2;
     area2 = PI * r * r;
     return area2;
}

void print (float Vol)
{
     printf("The volume of the figure is %f ", Vol);
 }
