# Skills Making Factory — Optimization Engine

## Purpose
The optimization-engine improves existing skills based on benchmark results, test feedback, and usage patterns. It focuses on making skills more accurate, reliable, efficient, and maintainable.

## Responsibilities
- Analyze benchmark results for performance bottlenecks in skills
- Identify skills with high execution time or resource consumption
- Propose optimizations for slow or inefficient skills
- Measure improvement from optimizations
- Maintain a library of proven optimization patterns

## Inputs
- Benchmark results from benchmark-engine
- Test results from testing-engine
- Skill performance metrics
- Optimization patterns library

## Outputs
- Optimization proposals: skills-factory/laboratories/prototypes/<skill-name>/optimization-proposal.md
- Optimization results: skills-factory/reports/optimization-results-<skill-name>.json
- Performance improvements: updated SKILL.md files

## Procedure
1. **Analyze Benchmarks**: Review benchmark results for slow or resource-intensive skills
2. **Identify Bottlenecks**: Determine which parts of a skill procedure are slow or inefficient
3. **Propose Optimization**: Design optimization that improves performance without reducing quality
4. **Apply Optimization**: Update the skill file with the optimization
5. **Re-test**: Run testing-engine to verify the optimized skill still passes
6. **Re-benchmark**: Run benchmark-engine to measure improvement
7. **Record Results**: Write optimization results report

## Safety & Governance
- **No quality regression**: Optimizations must not reduce accuracy or reliability
- **Evidence-based**: All optimizations backed by before/after benchmark evidence
- **Prototype first**: Optimizations tested in laboratories/prototypes/ before promotion

## Completion Criteria
- Optimization proposal documented
- Before/after benchmark comparison available
- Quality verified after optimization
- Results recorded
