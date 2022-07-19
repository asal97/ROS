
1. clone the repository
2. In order to run it on your machine first make sure that you are connected to the bot by running 

``` ping MY_ROBOT.local ```

3. then make sure that your robot has access to the internet :

``` ssh duckie@MY_ROBOT.local ```

**password is quackquack**

``` ping 8.8.8.8 ```

4. then inside the cloned repo run :

 ``` dts devel build -f -H MY_ROBOT.local ```
 
 ``` dts devel run -H MY_ROBOT.local```
