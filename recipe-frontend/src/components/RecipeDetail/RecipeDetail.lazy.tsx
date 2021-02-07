import React, { lazy, Suspense } from 'react';

const LazyRecipeDetail = lazy(() => import('./RecipeDetail'));

const RecipeDetail = (props: JSX.IntrinsicAttributes & { children?: React.ReactNode; }) => (
  <Suspense fallback={null}>
    <LazyRecipeDetail {...props} />
  </Suspense>
);

export default RecipeDetail;
