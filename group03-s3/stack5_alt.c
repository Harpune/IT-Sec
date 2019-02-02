#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void dummy()
{
  char buffer[64];

  gets(buffer);
}

int main(int argc, char **argv)
{
  dummy();
}
