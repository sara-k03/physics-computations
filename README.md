# Physics Computations
Below are descriptions of the scripts, separated by class/project. 
## PY203 - University Physics III (Modern Physics)
### EIC:
Link to the Lab Manual: https://drive.google.com/file/d/11XniXMiJR4cYK6svrC_m2AB7cFB1SyZQ/view 
### Homework 8: 
The only question in this folder is Question #17 from Section 8.2 of Modern Physics by Felder & Felder. The question is as follows: <br />
<br />
The effective screening felt by an outer electron depends on the radial probability distributions of both the outer and the inner electrons. 
In this problem you will numerically simulate the screening of the outer electron in lithium in both the 2s and 2p states. For simplicity we’re 
going to take a<sub>0</sub> = 1 throughout this problem. <br />
<br />
(a) Write the radial probability distributions P(r) = r<sup>2</sup>R<sub>nl</sub><sup>2</sup> for the 2s state of hydrogen. You can find the energy
eigenstates in Appendix G. <br />
<br />
(b) Generate a random electron from that probability distribution. To do that you can generate a random number r from 0 to 15, and another random number y from 0 to 1. 
(Make sure to generate random real numbers, not just integers.) If y < P(r) then r is your randomly generated radius. If it isn’t then generate a new pair of numbers r and 
y until you get one that works. (Think about why this gives you random numbers that obey this probability distribution. The upper limit 15 is chosen because the probability 
distribution is negligible beyond r = 15a<sup>0</sup>.)  <br />
<br />
(c) Use that procedure to generate 10,000 random radii drawn from the 2s probability distribution. For each one, let Z = 1 if r > 1 and Z = 3 if r < 1. Add all of the resulting 
Z-values and divide by 10,000 to get their average, Zeff. (If you don’t get a final average Zeff between 1 and 3 then you did something wrong.) <br />
<br />
(d) Repeat the entire procedure using the 2p distribution instead of 2s. <br />
<br />
(e) For which one did you find the larger value of Zeff? Why does this make sense? <br />
<br />
(f) The Zeff you found shouldn’t equal the actual one we said has been measured for lithium. Give at least two reasons why not. <br />

## PY203 - University Physics III (Modern Physics)
Contains datasets/analysis for data obtained from the Instron machine when compressing disordered network cubes. 
