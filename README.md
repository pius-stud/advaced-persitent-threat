# Advanced Perstitent Threat (APT)

Here a proof of concept of an Advanced Persistent Thereat could be found.
This is composed of different elements:
- Client (or Hacker): this (script) could be exploited by the hacker to give commands to the system.
- Command and Control center (CC): this is a bridge between the hacker and the target.
- Target: this receives the command(s) choosed by the hacker, which is executed and its result is sent back to the hacker through the CC.

Thanks to the implemented commands, the hacker could be able to get a list of the files in a choosen directory on the target's computer, to select one of these files and to encript it using asymmetric or symmetric cryptography. 
