import React,{useState,useEffect} from 'react';
import styles from './RecipeDetail.module.css';

export interface RecipeResponse {
  title: string;
  author: string;
}


const RecipeDetail: React.FC = (props) => {
  
  const [recipes, setRecipes] = useState<RecipeResponse[]>([]);
 
  useEffect(() => {
    async function getRecipes() {
      const response = await fetch('http://localhost:8000/recipes')
      if(response.ok){
        const fetchedRecipes = await response.json();
        setRecipes(fetchedRecipes);
        console.log(fetchedRecipes)
      }
    };
    getRecipes();
  }, [])

  return (
    <div className={styles.RecipeDetail}>
    {
      recipes.map((recipe:RecipeResponse,index:number)=>{
        return (<span><b key={index}>{recipe.title}</b> by {recipe.author}</span>);
      })}
    </div>
    );
};

export default RecipeDetail;
