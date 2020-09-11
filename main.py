#Author: Slava Hlushko vqh5091@psu.edu



def getGradePoint(letterGrade):
  
  if letterGrade == "A" or letterGrade == "a":
   gradepoint = 4.0;
   return gradepoint  

  elif letterGrade =="A-" or letterGrade == "a-":
   gradepoint = 3.67;
   return gradepoint

  elif letterGrade == "B+" or letterGrade == "b+":
   gradepoint = 3.33;
   return gradepoint

  elif letterGrade == "B" or letterGrade == "b":
   gradepoint = 3.0;
   return gradepoint

  elif letterGrade == "B-" or letterGrade == "b-":
   gradepoint = 2.67;
   return gradepoint

  elif letterGrade == "C+" or letterGrade == "c+":
   gradepoint = 2.33;
   return gradepoint

  elif letterGrade == "C" or letterGrade == "c":
   gradepoint = 2.0;
   return gradepoint

  elif letterGrade == "D" or letterGrade == "d":
   gradepoint = 1.0;
   return gradepoint

  else:
    gradepoint = 0.0;
    return gradepoint
  
  float(gradepoint)



#courselettergrade1=str(input("Enter your course 1 letter grade: "));
#coursecredit1=float(input("Enter your course 1 credit: "));
#print(f"Grade point for course 1 is: {getGradePoint(courselettergrade1)}.");

#courselettergrade2=str(input("Enter your course 2 letter grade: "));
#coursecredit2=float(input("Enter your course 2 credit: "));
#print(f"Grade point for course 2 is: {getGradePoint(courselettergrade2)}.");

#courselettergrade3=str(input("Enter your course 3 letter grade: "));
#coursecredit3=float(input("Enter your course 3 credit: "));
#print(f"Grade point for course 3 is: {getGradePoint(courselettergrade3)}.");

#gradepoint1 = getGradePoint(courselettergrade1)
#gradepoint2 = getGradePoint(courselettergrade2)
#gradepoint3 = getGradePoint(courselettergrade3)


#GPA = (gradepoint1 * coursecredit1 + gradepoint2 * coursecredit2 + gradepoint3 * coursecredit3) / (coursecredit1 + coursecredit2 + coursecredit3) 
#float(GPA);
#print(f"Your GPA is: {GPA}");

def run():
 courselettergrade1=str(input("Enter your course 1 letter grade: "));
 coursecredit1=float(input("Enter your course 1 credit: "));
 print(f"Grade point for course 1 is: {getGradePoint(courselettergrade1)}");

 courselettergrade2=str(input("Enter your course 2 letter grade: "));
 coursecredit2=float(input("Enter your course 2 credit: "));
 print(f"Grade point for course 2 is: {getGradePoint(courselettergrade2)}");

 courselettergrade3=str(input("Enter your course 3 letter grade: "));
 coursecredit3=float(input("Enter your course 3 credit: "));
 print(f"Grade point for course 3 is: {getGradePoint(courselettergrade3)}");

 gradepoint1 = getGradePoint(courselettergrade1)
 gradepoint2 = getGradePoint(courselettergrade2)
 gradepoint3 = getGradePoint(courselettergrade3)

 GPA = (gradepoint1 * coursecredit1 + gradepoint2 * coursecredit2 + gradepoint3 * coursecredit3) / (coursecredit1 + coursecredit2 + coursecredit3) 
 float(GPA);
 print(f"Your GPA is: {GPA}");
  

if __name__ == "__main__":
  run()