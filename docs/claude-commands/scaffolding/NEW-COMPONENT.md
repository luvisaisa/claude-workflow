# New Component

Scaffold React component with TypeScript and test.

## Arguments

- $COMPONENT_NAME — name of component (PascalCase, e.g., "AnnotationCard")
- $COMPONENT_TYPE — type: "page", "feature", "ui" (determines location)

## Steps

1. Read existing components to understand:
   - File structure conventions
   - Props interface patterns
   - Styling approach (Tailwind, CSS modules, etc.)
   - Import patterns

2. Determine location based on type:
   - page → `src/app/` or `src/pages/`
   - feature → `src/components/features/`
   - ui → `src/components/ui/`

3. Create component file: `{location}/{ComponentName}.tsx`
   ```typescript
   import { FC } from 'react';
   
   interface {ComponentName}Props {
     // Define props
   }
   
   export const {ComponentName}: FC<{ComponentName}Props> = (props) => {
     const { } = props;
     
     return (
       <div>
         {/* Component content */}
       </div>
     );
   };
   
   export default {ComponentName};
   ```

4. Create test file: `{location}/{ComponentName}.test.tsx`
   ```typescript
   import { render, screen } from '@testing-library/react';
   import { {ComponentName} } from './{ComponentName}';
   
   describe('{ComponentName}', () => {
     it('renders without crashing', () => {
       render(<{ComponentName} />);
       // Add assertions
     });
   });
   ```

5. Add to barrel export if exists: `{location}/index.ts`

6. Run verification:
   ```bash
   npm run lint -- --fix {location}/{ComponentName}.tsx
   npm run typecheck
   npm test -- --testPathPattern={ComponentName}
   ```

7. Report created files and test results
