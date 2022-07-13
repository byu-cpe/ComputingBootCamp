#ifndef GRAIN_H
#define GRAIN_H
#include "item.h"
#include "sstream"
class Grain : public Item
{
private:
    float weight;

public:
    Grain(std::string line) : Item(line)
    {
        weight = std::stof(extractNextAttribute(line));
    }
    Item::Type getType()
    {
        return GRAIN;
    }
    std::string toString()
    {
        std::stringstream output;
        output.precision(2);
        output << std::fixed;
        output << weight << " lb " << Item::toString();
        return output.str();
    }
};

#endif