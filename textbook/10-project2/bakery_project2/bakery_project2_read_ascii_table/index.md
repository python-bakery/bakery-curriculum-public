---
waltz:
  title: bakery_project2_read_ascii_table
  display title: 2) Ascii Table Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 19
    created: October 12 2022, 0311 PM
    modified: October 13 2022, 1005 AM
  files:
    path: bakery_project2_read_ascii_table
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
**MAKE SURE YOU COMPLETE THE QUIZ FOR THIS READING BEFORE YOU CONTINUE!**

The American Standard Code for Information Interchange (ASCII) is a way of representing text via numbers. Every single
character is represented via a different number. Although modern systems require a larger set, the basic ASCII table has
remained relatively unchanged since it was created in the 1960s. The system is critical to sending storing and
transmitting textual data. You can read more about the history of [ASCII here](https://en.wikipedia.org/wiki/ASCII).

# The Ord Function

To convert a single character (string) to an integer, use the built-in `ord` function. This function consumes a string
and produces an integer. The string must be exactly one character long, or you will get a TypeError.

```python try-ord
# Remember, you do not need to `print` to call a function like `ord`!
# We only need it here to see the results.

print(ord("A"))
# 65

print(ord("a"))
# 97

print(ord("6"))
# 54

print(ord("!"))
# 33

print(ord("FF"))
# TypeError!
```

# The Chr Function

To convert an integer back to a character (string), use the built-in `chr` function. This function consumes an
integerand produces a string. The integer must be a positive number, or you will get a `ValueError`. Values outside of
the range 32-126 are not printable, and may look weird when you try to convert them.

```python try-chr
# Remember, you do not need to `print` to call a function like `ord`!
# We only need it here to see the results.

print(chr(65))
# "A"

print(chr(97))
# "a"

print(chr(54))
# "6"

print(chr(33))
# "!"

print(chr(-1))
# ValueError!
```

# The ASCII Printable Characters

Codes 32-126 are common for all the different variations of the ASCII table. They are called printable characters,
representing letters, digits, punctuation marks, and a few miscellaneous symbols. You will find almost every character
on your keyboard.

Below, you can see all of the printable ASCII characters and their decimal representations.

<table class="table-bordered table-condensed table tbl table-striped table-sm table-hover table-responsive"><thead><tr><th>Char</th><th>Number</th><th>Description</th><th></th><th>Char</th><th>Number</th><th>Description</th><th></th><th>Char</th><th>Number</th><th>Description</th><th></th><th>Char</th><th>Number</th><th>Description</th></tr></thead><tbody><tr><td> </td><td>32</td><td>space</td><td></td><td>8</td><td>56</td><td>digit 8</td><td></td><td>P</td><td>80</td><td>uppercase P</td><td></td><td>h</td><td>104</td><td>lowercase h</td></tr><tr><td>!</td><td>33</td><td>exclamation mark</td><td></td><td>9</td><td>57</td><td>digit 9</td><td></td><td>Q</td><td>81</td><td>uppercase Q</td><td></td><td>i</td><td>105</td><td>lowercase i</td></tr><tr><td>"</td><td>34</td><td>quotation mark</td><td></td><td>:</td><td>58</td><td>colon</td><td></td><td>R</td><td>82</td><td>uppercase R</td><td></td><td>j</td><td>106</td><td>lowercase j</td></tr><tr><td>#</td><td>35</td><td>number sign</td><td></td><td>;</td><td>59</td><td>semicolon</td><td></td><td>S</td><td>83</td><td>uppercase S</td><td></td><td>k</td><td>107</td><td>lowercase k</td></tr><tr><td>$</td><td>36</td><td>dollar sign</td><td></td><td>&lt;</td><td>60</td><td>less-than</td><td></td><td>T</td><td>84</td><td>uppercase T</td><td></td><td>l</td><td>108</td><td>lowercase l</td></tr><tr><td>%</td><td>37</td><td>percent sign</td><td></td><td>=</td><td>61</td><td>equals-to</td><td></td><td>U</td><td>85</td><td>uppercase U</td><td></td><td>m</td><td>109</td><td>lowercase m</td></tr><tr><td>&amp;</td><td>38</td><td>ampersand</td><td></td><td>&gt;</td><td>62</td><td>greater-than</td><td></td><td>V</td><td>86</td><td>uppercase V</td><td></td><td>n</td><td>110</td><td>lowercase n</td></tr><tr><td>'</td><td>39</td><td>apostrophe</td><td></td><td>?</td><td>63</td><td>question mark</td><td></td><td>W</td><td>87</td><td>uppercase W</td><td></td><td>o</td><td>111</td><td>lowercase o</td></tr><tr><td>(</td><td>40</td><td>left parenthesis</td><td></td><td>@</td><td>64</td><td>at sign</td><td></td><td>X</td><td>88</td><td>uppercase X</td><td></td><td>p</td><td>112</td><td>lowercase p</td></tr><tr><td>)</td><td>41</td><td>right parenthesis</td><td></td><td>A</td><td>65</td><td>uppercase A</td><td></td><td>Y</td><td>89</td><td>uppercase Y</td><td></td><td>q</td><td>113</td><td>lowercase q</td></tr><tr><td>*</td><td>42</td><td>asterisk</td><td></td><td>B</td><td>66</td><td>uppercase B</td><td></td><td>Z</td><td>90</td><td>uppercase Z</td><td></td><td>r</td><td>114</td><td>lowercase r</td></tr><tr><td>+</td><td>43</td><td>plus sign</td><td></td><td>C</td><td>67</td><td>uppercase C</td><td></td><td>[</td><td>91</td><td>left square bracket</td><td></td><td>s</td><td>115</td><td>lowercase s</td></tr><tr><td>,</td><td>44</td><td>comma</td><td></td><td>D</td><td>68</td><td>uppercase D</td><td></td><td>\</td><td>92</td><td>backslash</td><td></td><td>t</td><td>116</td><td>lowercase t</td></tr><tr><td>-</td><td>45</td><td>hyphen</td><td></td><td>E</td><td>69</td><td>uppercase E</td><td></td><td>]</td><td>93</td><td>right square bracket</td><td></td><td>u</td><td>117</td><td>lowercase u</td></tr><tr><td>.</td><td>46</td><td>period</td><td></td><td>F</td><td>70</td><td>uppercase F</td><td></td><td>^</td><td>94</td><td>caret</td><td></td><td>v</td><td>118</td><td>lowercase v</td></tr><tr><td>/</td><td>47</td><td>slash</td><td></td><td>G</td><td>71</td><td>uppercase G</td><td></td><td>_</td><td>95</td><td>underscore</td><td></td><td>w</td><td>119</td><td>lowercase w</td></tr><tr><td>0</td><td>48</td><td>digit 0</td><td></td><td>H</td><td>72</td><td>uppercase H</td><td></td><td>`</td><td>96</td><td>grave accent</td><td></td><td>x</td><td>120</td><td>lowercase x</td></tr><tr><td>1</td><td>49</td><td>digit 1</td><td></td><td>I</td><td>73</td><td>uppercase I</td><td></td><td>a</td><td>97</td><td>lowercase a</td><td></td><td>y</td><td>121</td><td>lowercase y</td></tr><tr><td>2</td><td>50</td><td>digit 2</td><td></td><td>J</td><td>74</td><td>uppercase J</td><td></td><td>b</td><td>98</td><td>lowercase b</td><td></td><td>z</td><td>122</td><td>lowercase z</td></tr><tr><td>3</td><td>51</td><td>digit 3</td><td></td><td>K</td><td>75</td><td>uppercase K</td><td></td><td>c</td><td>99</td><td>lowercase c</td><td></td><td>{</td><td>123</td><td>left curly brace</td></tr><tr><td>4</td><td>52</td><td>digit 4</td><td></td><td>L</td><td>76</td><td>uppercase L</td><td></td><td>d</td><td>100</td><td>lowercase d</td><td></td><td>|</td><td>124</td><td>vertical bar</td></tr><tr><td>5</td><td>53</td><td>digit 5</td><td></td><td>M</td><td>77</td><td>uppercase M</td><td></td><td>e</td><td>101</td><td>lowercase e</td><td></td><td>}</td><td>125</td><td>right curly brace</td></tr><tr><td>6</td><td>54</td><td>digit 6</td><td></td><td>N</td><td>78</td><td>uppercase N</td><td></td><td>f</td><td>102</td><td>lowercase f</td><td></td><td>~</td><td>126</td><td>tilde</td></tr><tr><td>7</td><td>55</td><td>digit 7</td><td></td><td>O</td><td>79</td><td>uppercase O</td><td></td><td>g</td><td>103</td><td>lowercase g</td><td></td><td></td><td></td><td></td></tr></tbody></table>