// src/calculator/calculator.service.ts
import { Injectable } from '@nestjs/common';

@Injectable()
export class CalculadoraService {
  calculate(a: number, b: number, operation: string): number {
    switch (operation) {
      case 'sum': return a + b;
      case 'sub': return a - b;
      case 'mul': return a * b;
      case 'div':
        if (b === 0) throw new Error('Division by zero');
        return a / b;
      default: throw new Error('Invalid operation');
    }
  }
}
