# Bootstrap Progress Bar in Oracle APEX Report

Step 1: Create a new blank page.

Step 2: Add CSS to the page in inline CSS section. It will make the magic happen.
```
.progress-bar {
    display: -ms-flexbox;
    display: flex;
    -ms-flex-direction: column;
    flex-direction: column;
    -ms-flex-pack: center;
    justify-content: center;
    color: #fff;
    text-align: center;
    white-space: nowrap;
    background-color: #007bff;
    transition: width .6s ease;
}

.progress {
    display: -ms-flexbox;
    display: flex;
    height: 1rem;
    overflow: hidden;
    font-size: .75rem;
    background-color: #cfdae4;
    border-radius: .25rem;
}
```
Step 3: Function Call: Create a function get_progress_bar in util_pkg. If you want to render it in multiple places, it would be good practice to put this code in a package and call it in your query.
```
CREATE OR replace FUNCTION get_progress_bar (p_value IN VARCHAR) 
RETURN VARCHAR2 
IS 
  l_height NUMBER := 20; 
BEGIN 
    RETURN '<span>  <div class="progress" style="height:' 
           ||l_height 
           ||'px;"> <div class="progress-bar" style="width:' 
           ||p_value 
           ||'%">' 
           ||p_value 
           ||' % </div></div></span>'; 
END;
```
Step 4: Create a new classical report or interactive report (whichever you want), then your query would then look something like this,
```
SELECT task_name, start_date
       util_pkg.get_progress_bar(growth) growth
  FROM my_table ;
  ```
Step 5: Go to report attribute growth and set Escape special characters = Yes
