# lua-cjson RPM Builder

Automated RPM build of the lua-cjson module for Oracle Linux 8 / RHEL 8, optimized for use with Fluent Bit and other LuaJIT applications.

## 📋 Description

This repository provides an automated build of the [lua-cjson](https://github.com/openresty/lua-cjson) module packaged as RPM. The module enables JSON processing in Lua scripts, especially useful for custom filters in Fluent Bit.

## 🚀 Features

- **Smart Daily Checks**: Runs daily to detect new versions without unnecessary builds
- **Resource Optimization**: Only builds when new upstream versions are available
- **Automatic Version Detection**: Automatically detects the latest version from upstream repository
- **Optimized RPM**: Compiled specifically for Oracle Linux 8 / RHEL 8
- **LuaJIT Compatibility**: Optimized for LuaJIT 2.1+
- **Automatic Releases**: Generates GitHub releases with ready-to-download RPMs
- **Build Decision Transparency**: Clear logs showing why builds run or skip

## 📦 Installation

### From GitHub Releases

1. **Download the latest RPM**:
   ```bash
   # Get the latest version
   LATEST_VERSION=$(curl -s https://api.github.com/repos/arengifoc/lua-cjson/releases/latest | grep '"tag_name":' | cut -d'"' -f4)
   
   # Download the RPM
   wget https://github.com/arengifoc/lua-cjson/releases/download/$LATEST_VERSION/lua-cjson-*.rpm
   ```

2. **Install the RPM**:
   ```bash
   sudo dnf install -y ./lua-cjson-*.rpm
   ```

### System Requirements

- Oracle Linux 8 / RHEL 8 / CentOS 8
- LuaJIT >= 2.1.0

## 💻 Usage

### In Lua Scripts

```lua
local cjson = require "cjson"

-- Encode Lua table to JSON
local data = {
    name = "example",
    values = {1, 2, 3},
    active = true
}
local json_string = cjson.encode(data)
print(json_string)  -- {"name":"example","values":[1,2,3],"active":true}

-- Decode JSON to Lua table
local parsed = cjson.decode(json_string)
print(parsed.name)  -- example
```

### In Fluent Bit Filters

```lua
function filter_json_processor(tag, timestamp, record)
    local cjson = require "cjson"
    
    -- Process JSON field from record
    if record["json_field"] then
        local parsed = cjson.decode(record["json_field"])
        record["parsed_data"] = parsed
        record["json_field"] = nil  -- Remove original field
    end
    
    return 1, timestamp, record
end
```

## 🔧 Development

### Repository Structure

```
├── .github/workflows/
│   └── build.yml          # GitHub Actions workflow
├── SPECS/
│   └── lua-cjson.spec     # RPM specification
├── SOURCES/               # Sources (auto-generated)
└── README.md             # This file
```

### Build Workflow

The automated workflow is optimized for efficiency:

1. **Version Check** (runs daily at 6:00 AM UTC)
   - Checks for new lua-cjson versions from upstream
   - Compares with existing releases in this repository
   - **Skips build** if no new version is available (saves resources)

2. **Conditional Build** (only when needed)
   - **Compiles lua-cjson** with LuaJIT from the specific upstream version
   - **Generates the RPM** with detected version and dynamic changelog
   - **Creates GitHub release** with the RPM as downloadable asset

3. **Smart Resource Usage**
   - Daily runs consume minimal resources when no build is needed
   - Full build only executes when a new upstream version is detected
   - Manual execution always builds (useful for testing/debugging)

### Manual Execution

You can run the workflow manually from GitHub Actions:

1. Go to **Actions** → **Build lua-cjson RPM**
2. Click **Run workflow**
3. Select the branch (usually `develop`)
4. Execute the workflow

**Note**: Manual execution always performs a full build, regardless of whether a new version is available. This is useful for testing changes or forcing a rebuild.

### Workflow Behavior

The workflow has different behaviors depending on how it's triggered:

| Trigger | Behavior | Use Case |
|---------|----------|----------|
| **Daily Schedule** | Smart: Only builds if new version detected | Automatic monitoring |
| **Manual Execution** | Always builds | Testing, debugging, forced rebuilds |
| **Push to main/develop** | Always builds | Development workflow |
| **Tag push** | Always builds | Release workflow |

## 📋 RPM Specifications

- **Name**: `lua-cjson`
- **Architecture**: `x86_64`
- **Installation location**: `/usr/local/lib/lua/5.1/cjson.so`
- **Dependencies**: `luajit >= 2.1.0`
- **License**: MIT

## 🔗 Links

- **Original Repository**: [openresty/lua-cjson](https://github.com/openresty/lua-cjson)
- **Releases**: [GitHub Releases](https://github.com/arengifoc/lua-cjson/releases)
- **lua-cjson Documentation**: [Official documentation](https://github.com/openresty/lua-cjson#readme)
- **Fluent Bit**: [Lua filters documentation](https://docs.fluentbit.io/manual/pipeline/filters/lua)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📄 License

This packaging project is under the MIT license, same as the original lua-cjson project.

## ⚠️ Support

To report issues related to:

- **RPM packaging**: Open an issue in this repository
- **lua-cjson module**: Report in the [upstream repository](https://github.com/openresty/lua-cjson/issues)

---

**Note**: This is a packaging repository. The lua-cjson module source code is automatically obtained from the official OpenResty repository.
