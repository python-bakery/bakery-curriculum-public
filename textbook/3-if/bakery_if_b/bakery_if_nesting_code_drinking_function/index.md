---
waltz:
  title: bakery_if_nesting_code_drinking_function
  display title: 3B1.1) Drinking Function
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    start_view: text
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 7
    created: June 28 2022, 0300 PM
    modified: September 09 2022, 0256 PM
  files:
    path: bakery_if_nesting_code_drinking_function
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
<p>Create a function named <code>can_drink</code> that takes in <code>age</code> and <code>has_license</code>. Then, use your logic from question #25.2 as the function's body. Change the function's body to <em>return</em> strings (not print!). Call the function with your own information (again, or make it up) and unit test it. Note that you will need to get full coverage - think of many different test cases so that your unit tests try out every path through the code!</p><p></p><p>Here is the logic from #25.2:</p><pre>if you are 21 or older<br>    if you are less than 1000 years old<br>        if you have a license<br>            then return "Can drink"<br>        otherwise<br>            then return "Doesn't have a license"<br>    otherwise<br>        then return "Too old"<br>otherwise<br>    the return "Too young"<br></pre><p></p>