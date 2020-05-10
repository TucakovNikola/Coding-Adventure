# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#initiatiting
misc = list() #A Temp storage for words
filt = list() #B temp storage for words
product = tuple() #final product


# %%
def fclean(string): #funtion for removing special characters
      new_string = string
      badchar = (",", '"', "(", ")", ";", ":", ".", "[", "]", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "")
      for char in badchar:
            new_string = new_string.replace(char, "")

      return new_string


# %%
try:
    data = str(input("Enter file: "))
    with open(data, "r") as txt: #Closing IO is too much work
        for line in txt: #looping thru lines
            for word in line.lower().split(): #spliting words
                z = fclean(word)
                misc.append(z)
except:
    n = 128
    i = None
    for i in range(n):
        print("=", end="")
    print("\nFile failed to open")


# %%
word = None #don't wanna use a word from before and to keep it consistent
for word in misc: #filter
    if word not in filt:
        filt.append(word)


# %%
i = None #never forget
filt = [i for i in filt if i] #list compression
product = sorted(filt)


# %%
print("There were %i words used in the file in which %i were unique.\n" % (len(misc), len(filt)))
print("The sorted list of unique words")


# %%
with open("sorted list.txt", mode="w", encoding="utf-8") as res:
    for i in product:
        res.write("%s\n" % i)

