# Claude Code Presentation

## Slide 1: Introduction - Getting Started
```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Start a new session
claude

# Start with a specific query
claude "analyze this codebase"

# Update to latest version
claude update
```

## Slide 2: Session Management
```bash
# Continue most recent conversation
claude -c
claude --continue

# Resume a specific past session
claude -r
claude --resume

# Non-interactive query (SDK mode)
claude -p "query"

# Process piped content
cat file.txt | claude -p "explain this code"
```

## Slide 3: Essential Slash Commands
```
/help       - List all available commands
/clear      - Reset conversation history
/compact    - Summarize conversation to reduce tokens
/init       - Create CLAUDE.md for project context
/model      - Switch between Claude models
/review     - Request code/PR review
```

## Slide 4: Advanced CLI Flags
```bash
# Add additional working directories
claude --add-dir /path/to/dir

# Specify allowed tools
claude --allowedTools Read,Write,Bash

# Set specific model
claude --model claude-sonnet-4

# Enable verbose logging
claude --verbose

# Limit agentic turns
claude --max-turns 10

# Output as JSON for scripting
claude --output-format json
```

## Slide 5: Model Context Protocol (MCP)
```bash
# Configure MCP servers
claude mcp

# Add MCP extensions
claude mcp add playwright
claude mcp add [service-name]
```

## Slide 6: Common Query Patterns
```
> summarize this project
> explain the folder structure
> find files that handle user authentication
> explain the main architecture patterns
> ultrathink [complex problem]
```

## Slide 7: Custom Workflows
**Project Context**
- Create `.claude/CLAUDE.md` for project-specific instructions
- Create custom slash commands in `.claude/commands/`

**Token Usage Tracking**
```bash
npx ccusage@latest
```

**Custom Agents**
```bash
claude --agents '{"name": "agent-name", "description": "...", "prompt": "..."}'
```

## Slide 8: Best Practices
- Use `/init` to create project context early
- Use `/compact` when conversations get long
- Use `--add-dir` for multi-directory projects
- Create custom commands for repeated workflows
- Track token usage with `ccusage`
- Leverage MCP for extended capabilities
