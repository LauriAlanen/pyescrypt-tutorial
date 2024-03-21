# Yescrypt Parameters

In the **/etc/shadow** file passwords hashed with **yescrypt**, usually have this `j9T` **parameter** as shown in the following example shadow entry, but information about this parameter is hard to come by.

`test_user_1:$6$j9T$xyz$VKswtvLoVpOLcpjDMIFXhxa8ukqqKSKHjcPBLZUk9NxWldmlFQY4stUGo.QjEhav7mp86ih2PRqYPqjkhWi5y.:19796:0:99999:7:::`

When you create a user using `adduser test_user_1`, you are might never see this `j9T` change, but now you might question what does this parameter even do?

## Yescrypt Parameter j9T

Let's look at creating a yescrypt hash using python with the following line `hasher = Yescrypt(n=2 ** 16, r=1, p=1, mode=Mode.MCF)`

Code for this example can be found here [GitHub Repo](https://github.com/LauriAlanen/pyescrypt-tutorial/blob/main/pyescrypt-example.py)

The important parameters in this case are

- **n** amount of **blocks**
- **r** size of the **blocks** in 128-byte units so for example in `j9T` it's $9\cdot128 = 1152 bytes$
- **p** amount of paraller **threads** run

Recomended paremeters for different setups can be found **[here](https://github.com/openwall/yescrypt/blob/main/PARAMETERS)**

## So `j9T` Means What?

- **J** Seems to be the same no matter the parameters.
- The **second** parameter is the amount of blocks, the value of the second parameter can be calculated using $8\cdot 2^n$, where $n$ is the block parameter value so in this case $9$, which results in $8\cdot 2^9=4096\ blocks$. **Note!!** If this parameters is bigger than 9 rather than showing numbers 10 etc, letters are shown in alphabetical order, so 10 would be **A**.
- Third parameter is the size of the **blocks** the formula for calculating the size of the blocks is $3+n$, so in this case, we know that $T$ is the $20th$ alphabet, and the alphabetical counting starts after $9$ so, $block_{size}=3+9+20=32 \Rightarrow T$.
