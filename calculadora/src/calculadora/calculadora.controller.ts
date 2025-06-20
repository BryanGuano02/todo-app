// src/calculator/calculator.controller.ts
import { Controller, Get, Query } from '@nestjs/common';
import { CalculadoraService } from './calculadora.service';

@Controller('calculadora')
export class CalculadoraController {
  constructor(private readonly calculadoraService: CalculadoraService) {}

  @Get()
  getResult(
    @Query('a') a: string,
    @Query('b') b: string,
    @Query('op') op: string,
  ) {
    const numA = parseFloat(a);
    const numB = parseFloat(b);
    const result = this.calculadoraService.calculate(numA, numB, op);
    return { result };
  }
}
